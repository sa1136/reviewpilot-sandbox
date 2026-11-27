from django.contrib.postgres.operations import AddIndexConcurrently
from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("analytics", "0001_initial"),
    ]

    operations = [
        AddIndexConcurrently(
            model_name="pageview",
            index=models.Index(fields=["session_key", "created_at"], name="analytics_pv_session_created"),
        ),
    ]
