# Generated by Django 4.1.4 on 2022-12-19 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, max_length=100)),
            ],
        ),
    ]