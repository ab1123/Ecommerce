# Generated by Django 4.1.1 on 2023-02-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_alter_product_details"),
    ]

    operations = [
        migrations.CreateModel(
            name="Appliances",
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
                ("pid", models.CharField(blank=True, max_length=20, null=True)),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("details", models.TextField(blank=True, max_length=20000, null=True)),
                ("price", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Electronics",
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
                ("pid", models.CharField(blank=True, max_length=20, null=True)),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("details", models.TextField(blank=True, max_length=20000, null=True)),
                ("price", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Kids",
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
                ("pid", models.CharField(blank=True, max_length=20, null=True)),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("details", models.TextField(blank=True, max_length=20000, null=True)),
                ("price", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Men",
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
                ("pid", models.CharField(blank=True, max_length=20, null=True)),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("details", models.TextField(blank=True, max_length=20000, null=True)),
                ("price", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Pets",
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
                ("pid", models.CharField(blank=True, max_length=20, null=True)),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("details", models.TextField(blank=True, max_length=20000, null=True)),
                ("price", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Women",
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
                ("pid", models.CharField(blank=True, max_length=20, null=True)),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("details", models.TextField(blank=True, max_length=20000, null=True)),
                ("price", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="Product",
        ),
    ]