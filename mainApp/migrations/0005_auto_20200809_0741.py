# Generated by Django 3.1 on 2020-08-09 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20200809_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcar',
            name='image',
            field=models.ImageField(upload_to='media/addcars'),
        ),
        migrations.AlterField(
            model_name='sellcar',
            name='image',
            field=models.ImageField(upload_to='media/sellcars'),
        ),
    ]
