# Generated by Django 4.1.5 on 2023-02-13 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_organapplicationmodels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organapplicationmodels',
            name='Donate_Organ',
            field=models.CharField(max_length=50000, null=True),
        ),
    ]
