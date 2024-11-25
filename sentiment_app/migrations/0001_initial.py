# Generated by Django 5.1.3 on 2024-11-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SentimentLog",
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
                ("text", models.TextField()),
                ("sentiment", models.CharField(max_length=20)),
                ("polarity", models.FloatField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]