# Generated by Django 5.0.4 on 2024-05-10 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_sitter_babe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitter',
            name='babe',
        ),
    ]
