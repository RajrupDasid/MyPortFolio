# Generated by Django 3.2.6 on 2021-08-13 05:08

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioweb', '0019_rename_background_pageimage_imageview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('careersummary', ckeditor_uploader.fields.RichTextUploadingField()),
                ('biography', ckeditor_uploader.fields.RichTextUploadingField()),
                ('skills', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]