import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PageView",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("path", models.CharField(max_length=512)),
                ("session_key", models.CharField(blank=True, max_length=40)),
                ("referrer", models.CharField(blank=True, max_length=512)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("user", models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "indexes": [models.Index(fields=["created_at"], name="analytics_pv_created")],
            },
        ),
    ]
