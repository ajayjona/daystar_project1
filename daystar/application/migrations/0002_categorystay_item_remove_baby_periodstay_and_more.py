# Generated by Django 5.0.4 on 2024-05-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorystay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('current_stock', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='baby',
            name='periodstay',
        ),
        migrations.RemoveField(
            model_name='pay',
            name='description',
        ),
        migrations.RemoveField(
            model_name='pay',
            name='payment_sitter',
        ),
        migrations.RemoveField(
            model_name='sitter',
            name='fees',
        ),
        migrations.RemoveField(
            model_name='sitter',
            name='message_left',
        ),
        migrations.AddField(
            model_name='baby',
            name='babynumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='baby',
            name='fees',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='baby',
            name='stay_duration',
            field=models.CharField(blank=True, default='Fullday', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='baby',
            name='timein',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='baby',
            name='timeout',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pay',
            name='pay_status',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='sitter',
            name='contact',
            field=models.CharField(default=1, max_length=20),
        ),
        migrations.AlterField(
            model_name='baby',
            name='image',
            field=models.ImageField(max_length=255, upload_to=''),
        ),
    ]
