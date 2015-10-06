# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name': 'Pa\xeds',
                'verbose_name_plural': 'Pa\xedses',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_image', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('birth_date', models.DateField()),
                ('mothers_name', models.CharField(max_length=200)),
                ('fathers_name', models.CharField(max_length=200)),
                ('birth_local', models.CharField(max_length=150)),
                ('passport', models.CharField(max_length=50)),
                ('permanent_address', models.CharField(max_length=200)),
                ('permanent_phone', models.CharField(max_length=20)),
                ('nationality', models.ForeignKey(to='tracking.Country')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
        ),
    ]
