# Generated by Django 5.0.4 on 2024-05-15 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0015_pay_stay_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='stay_duration',
            field=models.CharField(choices=[('fullday', 'fullday'), ('halfday', 'halfday')], max_length=50),
        ),
    ]
