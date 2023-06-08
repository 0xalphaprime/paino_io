
# Generated by Django 4.2.2 on 2023-06-08 12:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sales_dashboard", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookedRevenue",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "embed_url",
                    models.URLField(
                        default="https://www.google.com/search?client=firefox-b-1-d&q=coding+for+dummies",
                        max_length=500,
                    ),
                ),
            ],
        ),
    ]