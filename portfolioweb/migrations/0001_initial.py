# Generated by Django 3.2.6 on 2021-08-07 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('contact', models.IntegerField()),
                ('bio', models.TextField()),
                ('address', models.TextField()),
                ('profile_image', models.ImageField(upload_to='profile_image')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
