# Generated by Django 3.2.6 on 2021-08-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioweb', '0016_contact_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='background',
            field=models.ImageField(default='contact.png', upload_to='contactsectionbackground'),
        ),
    ]
