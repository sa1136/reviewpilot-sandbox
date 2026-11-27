from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from catalog.models import Product
from catalog.serializers import product_json


def product_list(request):
    products = Product.objects.filter(active=True).order_by("name")
    return JsonResponse({"products": [product_json(p) for p in products]})


def product_detail(request, sku):
    product = get_object_or_404(Product, sku=sku, active=True)
    return JsonResponse(product_json(product))
