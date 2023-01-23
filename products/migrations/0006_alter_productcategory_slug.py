# Generated by Django 3.2.13 on 2023-01-23 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_productcategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
