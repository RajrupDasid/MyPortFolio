# Generated by Django 3.2.6 on 2021-08-14 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioweb', '0023_detailedportfolio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailedportfolio',
            name='section',
        ),
        migrations.AddField(
            model_name='detailedportfolio',
            name='identify',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
