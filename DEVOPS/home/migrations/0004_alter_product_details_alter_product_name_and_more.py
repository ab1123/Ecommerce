# Generated by Django 4.1.1 on 2023-02-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="details",
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="pid",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
