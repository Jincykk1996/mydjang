# Generated by Django 2.2.4 on 2019-10-14 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20191014_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 14, 14, 23, 40, 273779)),
        ),
    ]