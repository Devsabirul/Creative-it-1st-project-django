# Generated by Django 4.1.6 on 2023-03-05 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crudApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="image",
            field=models.ImageField(
                blank=True, default="default/default.png", null=True, upload_to="t/"
            ),
        ),
    ]