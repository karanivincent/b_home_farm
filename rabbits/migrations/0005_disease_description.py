# Generated by Django 3.0.6 on 2020-11-17 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rabbits', '0004_auto_20201117_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
