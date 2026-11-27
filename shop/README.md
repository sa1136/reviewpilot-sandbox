# shop

Django storefront API: catalog, checkout, accounts, page analytics.

## Run locally

    uv sync
    export DJANGO_SECRET_KEY=dev DJANGO_DEBUG=1
    uv run python manage.py migrate
    uv run python manage.py runserver

Tests: `uv run pytest`.

## Deploy

Every merge to `main` deploys. The release step runs `python manage.py migrate` against the
primary database, then the new web containers start (rolling, 6 containers).

Scheduled jobs (cron on the worker box, see `ops/crontab`):

- `purge_pageviews` daily at 03:00 UTC
- `recalculate_loyalty_tiers` daily at 04:30 UTC
