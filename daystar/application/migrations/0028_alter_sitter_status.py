# Generated by Django 5.0.4 on 2024-05-16 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0027_alter_sitter_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
