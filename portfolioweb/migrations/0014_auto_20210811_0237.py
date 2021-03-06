# Generated by Django 3.2.6 on 2021-08-11 02:37

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioweb', '0013_remove_portfolio_portfolio_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='bio',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='myportfolio',
            name='biography',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='myportfolio',
            name='careersummary',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='myportfolio',
            name='skills',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
