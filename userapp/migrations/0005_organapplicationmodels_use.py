# Generated by Django 4.1.5 on 2023-02-15 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_organapplicationmodels_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='organapplicationmodels',
            name='use',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.registrationmodels'),
        ),
    ]