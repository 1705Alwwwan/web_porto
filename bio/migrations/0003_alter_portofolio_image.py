# Generated by Django 5.1.4 on 2025-02-15 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bio", "0002_portofolio_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portofolio",
            name="image",
            field=models.ImageField(
                blank=True, default="default.png", null=True, upload_to="images/"
            ),
        ),
    ]
