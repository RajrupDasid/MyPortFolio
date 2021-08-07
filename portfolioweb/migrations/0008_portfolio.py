# Generated by Django 3.2.6 on 2021-08-07 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioweb', '0007_details_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('portfolio_image', models.ImageField(upload_to='Portfolio_images')),
            ],
        ),
    ]
