from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sku", models.CharField(max_length=40, unique=True)),
                ("name", models.CharField(max_length=200)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("sale_price", models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
    ]
