# Generated by Django 5.0.3 on 2024-03-19 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_price_efort_trip_price_confort'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
