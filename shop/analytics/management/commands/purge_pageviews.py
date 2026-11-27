from datetime import timedelta

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from analytics.models import PageView

BATCH = 10_000


class Command(BaseCommand):
    help = "Delete page views older than PAGE_VIEW_RETENTION_DAYS, in batches."

    def handle(self, *args, **options):
        cutoff = timezone.now() - timedelta(days=settings.PAGE_VIEW_RETENTION_DAYS)
        deleted = 0
        while True:
            ids = list(
                PageView.objects.filter(created_at__lt=cutoff).values_list("id", flat=True)[:BATCH]
            )
            if not ids:
                break
            PageView.objects.filter(id__in=ids).delete()
            deleted += len(ids)
        self.stdout.write(f"deleted {deleted} page views")
