# Generated by Django 3.1.5 on 2021-01-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EnrollmentRecord",
            fields=[
                ("_first_name", models.CharField(max_length=60)),
                ("_last_name", models.CharField(max_length=60)),
                ("_uuid", models.UUIDField(primary_key=True, serialize=False)),
                (
                    "_status",
                    models.CharField(
                        choices=[
                            ("PENDING", "Pending"),
                            ("IN PROGRESS", "In Progress"),
                            ("SUCCESSFUL", "Successful"),
                            ("FAILED", "Failed"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
