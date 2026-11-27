from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

RESET_URL = "https://shop.example/reset/{uid}/{token}/"


def send_reset_email(user) -> None:
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    send_mail(
        "Reset your password",
        f"Use this link to choose a new password: {RESET_URL.format(uid=uid, token=token)}",
        None,
        [user.email],
    )
