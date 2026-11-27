from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0002_order_shipping_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="shipping_country",
            field=models.CharField(default="US", max_length=2),
        ),
    ]
