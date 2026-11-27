from django.http import JsonResponse
from django.views.decorators.http import require_POST

from accounts.emails import send_reset_email
from accounts.services import get_user_by_email


@require_POST
def request_password_reset(request):
    email = request.POST.get("email", "")
    user = get_user_by_email(email)
    if user is not None and user.is_active:
        send_reset_email(user)
    # Same answer whether or not the account exists.
    return JsonResponse({"ok": True})
