# Generated by Django 3.1.7 on 2021-05-04 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20210501_0724'),
    ]

    operations = [
        migrations.CreateModel(
            name='smartfar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]