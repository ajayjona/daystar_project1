# Generated by Django 5.0.4 on 2024-05-16 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0028_alter_sitter_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitter',
            name='sit',
        ),
        migrations.AlterField(
            model_name='sitter',
            name='status',
            field=models.CharField(blank=True, default=False, max_length=10, null=True),
        ),
    ]
