# Generated by Django 3.2.6 on 2021-08-11 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioweb', '0012_auto_20210811_0211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='portfolio_image',
        ),
    ]