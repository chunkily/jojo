# Generated by Django 4.1.7 on 2023-03-03 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Away",
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
                ("userid", models.CharField(max_length=200)),
                ("start_on", models.DateTimeField()),
                ("end_on", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Deleted",
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
                ("deleted_on", models.DateTimeField()),
                ("obj_json", models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="Holiday",
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
                ("start_on", models.DateTimeField()),
                ("end_on", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(max_length=200)),
                ("standup_schedule", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="StandUpReport",
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
                ("userid", models.CharField(max_length=200)),
                ("submitted_on", models.DateTimeField()),
                ("what_you_did", models.TextField(max_length=1000)),
                ("what_you_plan_to_do", models.TextField(max_length=1000)),
                ("blockers", models.TextField(max_length=1000)),
                ("others", models.TextField(max_length=1000)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="app.project"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjectUser",
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
                ("userid", models.CharField(max_length=200)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="app.project"
                    ),
                ),
            ],
        ),
    ]
