# Generated by Django 3.0.6 on 2020-11-17 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rabbits', '0003_auto_20201117_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthlot',
            name='buck',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='father_of', to='rabbits.Rabbit'),
        ),
    ]
