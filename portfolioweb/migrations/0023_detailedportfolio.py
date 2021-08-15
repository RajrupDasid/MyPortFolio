# Generated by Django 3.2.6 on 2021-08-14 04:14

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioweb', '0022_auto_20210813_0529'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailedPortFolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.TextField()),
                ('detailed_career_summary', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]