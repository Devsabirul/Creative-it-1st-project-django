# Generated by Django 4.1.6 on 2023-03-05 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crudApp", "0002_alter_customer_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="image",
            field=models.ImageField(
                blank=True,
                default="default/default.png",
                null=True,
                upload_to="Profile Picture/",
            ),
        ),
    ]
