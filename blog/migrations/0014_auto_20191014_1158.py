# Generated by Django 2.2.4 on 2019-10-14 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20191011_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='cuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Author'),
        ),
    ]
