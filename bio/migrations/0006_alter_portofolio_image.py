# Generated by Django 5.1.4 on 2025-02-15 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bio", "0005_alter_portofolio_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portofolio",
            name="image",
            field=models.ImageField(
                blank=True, default="default.png", null=True, upload_to="image/"
            ),
        ),
    ]
