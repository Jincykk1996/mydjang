# Generated by Django 2.2.4 on 2019-10-14 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190902_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
    ]