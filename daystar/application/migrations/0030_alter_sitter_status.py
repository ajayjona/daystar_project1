# Generated by Django 5.0.4 on 2024-05-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0029_remove_sitter_sit_alter_sitter_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='status',
            field=models.CharField(blank=True, default='Available', max_length=10),
        ),
    ]
