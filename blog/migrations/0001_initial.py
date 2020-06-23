# Generated by Django 3.0.7 on 2020-06-23 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'categoeris',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=129)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'series',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('view', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/%Y/%m/%d/')),
                ('date_stamp', models.DateTimeField(auto_now_add=True)),
                ('edited', models.BooleanField(default=False)),
                ('time_edited', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(related_name='category', to='blog.Category')),
                ('dislike', models.ManyToManyField(blank=True, related_name='dislike', to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL)),
                ('series', models.ManyToManyField(blank=True, related_name='series', to='blog.Series')),
            ],
            options={
                'ordering': ['-view'],
            },
        ),
    ]
