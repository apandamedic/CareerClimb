# Generated by Django 5.1.1 on 2024-11-14 03:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JobListing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_name", models.CharField(max_length=255)),
                ("job_title", models.CharField(max_length=255)),
                ("post_url", models.URLField()),
                ("location", models.CharField(max_length=255)),
                ("work_style", models.CharField(max_length=255)),
                ("salary", models.CharField(max_length=255)),
                ("status", models.CharField(max_length=255)),
                ("deadline", models.DateField()),
                ("contacts", models.CharField(blank=True, max_length=255, null=True)),
                ("notes", models.TextField(blank=True, null=True)),
            ],
        ),
    ]