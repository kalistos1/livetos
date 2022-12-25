# Generated by Django 4.1.4 on 2022-12-18 13:10

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image', models.ImageField(blank=True, default='post.jpg', null=True, upload_to='post_images')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='post_images/')),
                ('tags', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_Updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'posts',
                'db_table': 'posts',
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
            options={
                'verbose_name_plural': 'comments',
                'db_table': 'comments',
                'ordering': ('-date_created',),
            },
        ),
    ]
