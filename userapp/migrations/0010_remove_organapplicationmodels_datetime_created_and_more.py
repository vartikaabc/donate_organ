# Generated by Django 4.1.5 on 2023-02-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_rename_user_organapplicationmodels_use'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organapplicationmodels',
            name='datetime_created',
        ),
        migrations.AddField(
            model_name='organapplicationmodels',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='organapplicationmodels',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='organapplicationmodels',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
