from datetime import datetime, time, timedelta, timezone

from django.db.models import Count

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


def session_journey(session_key: str, since) -> list[str]:
    """Paths one session visited since a datetime, in order."""
    return list(
        PageView.objects.filter(session_key=session_key, created_at__gte=since)
        .order_by("created_at")
        .values_list("path", flat=True)
    )
