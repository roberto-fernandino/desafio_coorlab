# Generated by Django 5.0.3 on 2024-03-19 00:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='trip',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.city'),
        ),
    ]
