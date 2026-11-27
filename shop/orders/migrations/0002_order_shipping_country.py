from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="shipping_country",
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
