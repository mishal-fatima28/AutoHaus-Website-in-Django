# Generated by Django 3.1 on 2020-08-09 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20200809_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcar',
            name='image',
            field=models.ImageField(upload_to='addcars'),
        ),
        migrations.AlterField(
            model_name='sellcar',
            name='image',
            field=models.ImageField(upload_to='sellcars'),
        ),
    ]
