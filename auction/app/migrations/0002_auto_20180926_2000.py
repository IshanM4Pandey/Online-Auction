# Generated by Django 2.1.1 on 2018-09-26 14:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 27, 14, 30, 50, 145858, tzinfo=utc)),
        ),
    ]