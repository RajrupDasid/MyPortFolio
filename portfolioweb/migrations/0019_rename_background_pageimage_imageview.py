# Generated by Django 3.2.6 on 2021-08-11 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioweb', '0018_auto_20210811_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pageimage',
            old_name='background',
            new_name='imageview',
        ),
    ]
