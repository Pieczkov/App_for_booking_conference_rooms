# Generated by Django 4.1.1 on 2022-09-17 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0006_roomreservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomreservation',
            name='date',
            field=models.DateField(),
        ),
    ]
