from django.conf import settings
from django.db import models


class PageView(models.Model):
    path = models.CharField(max_length=512)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, db_constraint=False
    )
    session_key = models.CharField(max_length=40, blank=True)
    referrer = models.CharField(max_length=512, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=["created_at"], name="analytics_pv_created")]
