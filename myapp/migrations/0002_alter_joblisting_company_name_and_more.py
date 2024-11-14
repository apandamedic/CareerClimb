# Generated by Django 5.1.1 on 2024-11-14 20:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="joblisting",
            name="company_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="joblisting",
            name="job_title",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="joblisting",
            name="location",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="joblisting",
            name="salary",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="joblisting",
            name="status",
            field=models.CharField(
                choices=[
                    ("wishlist", "Wishlist"),
                    ("applied", "Applied"),
                    ("interviewing", "Interviewing"),
                    ("follow-up", "Follow Up"),
                    ("offer", "Offer"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="joblisting",
            name="work_style",
            field=models.CharField(
                choices=[
                    ("hybrid", "Hybrid"),
                    ("on-site", "On Site"),
                    ("remote", "Remote"),
                ],
                max_length=20,
            ),
        ),
    ]
