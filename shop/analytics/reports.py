from datetime import datetime, time, timedelta, timezone

from django.db.models import Count
from django.db.models.functions import TruncDate

from analytics.models import PageView


def day_bounds(day):
    start = datetime.combine(day, time.min, tzinfo=timezone.utc)
    return start, start + timedelta(days=1)


def daily_views(day) -> int:
    start, end = day_bounds(day)
    return PageView.objects.filter(created_at__gte=start, created_at__lt=end).count()


def daily_visitors(day) -> int:
    start, end = day_bounds(day)
    return (
        PageView.objects.filter(created_at__gte=start, created_at__lt=end)
        .exclude(session_key="")
        .aggregate(n=Count("session_key", distinct=True))["n"]
    )


def views_for_path(path: str, since, until) -> list[dict]:
    """Views per day for one page between two datetimes."""
    return list(
        PageView.objects.filter(path=path, created_at__gte=since, created_at__lt=until)
        .annotate(day=TruncDate("created_at"))
        .values("day")
        .annotate(views=Count("id"))
        .order_by("day")
    )
