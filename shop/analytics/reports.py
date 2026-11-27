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
