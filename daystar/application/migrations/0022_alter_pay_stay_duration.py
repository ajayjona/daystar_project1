# Generated by Django 5.0.4 on 2024-05-15 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0021_remove_baby_stay_duration_alter_pay_stay_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='stay_duration',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
