# Generated by Django 3.1.7 on 2021-05-23 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MYS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mys',
            name='price',
            field=models.IntegerField(),
        ),
    ]