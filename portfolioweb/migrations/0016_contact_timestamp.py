# Generated by Django 3.2.6 on 2021-08-11 07:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioweb', '0015_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
