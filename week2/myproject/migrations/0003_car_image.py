# Generated by Django 2.0.1 on 2018-02-28 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0002_car_rent'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(default=2.37, upload_to='media'),
            preserve_default=False,
        ),
    ]
