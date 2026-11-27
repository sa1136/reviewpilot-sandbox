from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analytics", "0001_initial"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="pageview",
            index=models.Index(fields=["path", "created_at"], name="analytics_pv_path_created"),
        ),
    ]
