import json
from datetime import date, datetime, time, timedelta, timezone

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseBadRequest, JsonResponse, StreamingHttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from catalog.models import Product
from orders.checkout import CheckoutError, place_order
from orders.exports import iter_orders_csv
from orders.models import Order
from orders.money import format_cents
from orders.payments import PaymentDeclined


@require_POST
def checkout(request):
    data = json.loads(request.body)
    skus = {item["sku"]: int(item["quantity"]) for item in data["items"]}
    products = Product.objects.filter(sku__in=skus, active=True)
    lines = [(p, skus[p.sku]) for p in products if skus[p.sku] > 0]
    try:
        order = place_order(
            data["email"], lines, data["payment_token"], data.get("shipping_country")
        )
    except CheckoutError as exc:
        return JsonResponse({"error": str(exc)}, status=400)
    except PaymentDeclined as exc:
        return JsonResponse({"error": str(exc)}, status=402)
    return JsonResponse({"order_id": order.id, "total": format_cents(order.total_cents)})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    return JsonResponse(
        {
            "id": order.id,
            "status": order.status,
            "total": format_cents(order.total_cents),
            "lines": [
                {"sku": line.product.sku, "quantity": line.quantity}
                for line in order.lines.select_related("product")
            ],
        }
    )


def _day_start(value: str) -> datetime:
    return datetime.combine(date.fromisoformat(value), time.min, tzinfo=timezone.utc)


@user_passes_test(lambda u: u.is_staff)
def export_orders(request):
    """CSV of orders between ?start= and ?end= (ISO dates, end exclusive). Default: last 30 days."""
    today = datetime.now(timezone.utc).date()
    try:
        start = _day_start(request.GET.get("start") or (today - timedelta(days=30)).isoformat())
        end = _day_start(request.GET.get("end") or today.isoformat())
    except ValueError:
        return HttpResponseBadRequest("start and end must be YYYY-MM-DD")
    if end <= start:
        return HttpResponseBadRequest("end must be after start")
    response = StreamingHttpResponse(iter_orders_csv(start, end), content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="orders-{start:%Y%m%d}.csv"'
    return response
