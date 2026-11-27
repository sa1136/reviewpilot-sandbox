# Production database notes (shop)

Postgres 16, one primary and one read replica. Sizes from `pg_stat_user_tables` on 2026-10-01.

| Table | Rows (approx.) | Growth |
|---|---|---|
| accounts_user | 1.3M | about 2k new accounts a day |
| catalog_product | 18k | |
| orders_order | 14M | about 9k orders a day |
| orders_orderline | 41M | |
| analytics_pageview | 590M | one row per HTML page served; 400 day retention |

Peak traffic is about 450 HTML page requests a second (weekday evenings, US time).
