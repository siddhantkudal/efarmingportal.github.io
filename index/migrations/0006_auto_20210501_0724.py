# Generated by Django 3.1.7 on 2021-05-01 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20210501_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='uploaded/images'),
        ),
    ]