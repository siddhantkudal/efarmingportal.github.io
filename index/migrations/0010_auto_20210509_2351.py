# Generated by Django 3.1.7 on 2021-05-09 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='datetime',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
