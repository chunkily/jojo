# Generated by Django 4.1.7 on 2023-03-03 16:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="deleted",
            name="obj_type",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
    ]
