# Generated by Django 5.0.4 on 2024-05-15 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0022_alter_pay_stay_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pay',
            name='stay_duration',
        ),
    ]
