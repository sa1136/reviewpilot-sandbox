import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("catalog", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.CharField(choices=[("pending", "Pending"), ("paid", "Paid"), ("shipped", "Shipped"), ("cancelled", "Cancelled")], default="pending", max_length=10)),
                ("total_cents", models.IntegerField()),
                ("currency", models.CharField(default="USD", max_length=3)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("customer", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="orders", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="OrderLine",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quantity", models.PositiveIntegerField()),
                ("unit_price_cents", models.IntegerField()),
                ("order", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="lines", to="orders.order")),
                ("product", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="catalog.product")),
            ],
        ),
    ]
