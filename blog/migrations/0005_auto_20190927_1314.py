# Generated by Django 2.2.4 on 2019-09-27 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_msgcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='ddescription',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='dimage',
            field=models.ImageField(default=None, null=True, upload_to='pics'),
        ),
    ]