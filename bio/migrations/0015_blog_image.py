# Generated by Django 5.1.4 on 2025-02-25 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bio", "0014_course_end_date_course_is_current"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                blank=True, default="default.png", null=True, upload_to="image/"
            ),
        ),
    ]
