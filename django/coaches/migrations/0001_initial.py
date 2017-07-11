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
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_of_bitrh', models.DateField()),
                ('gender', models.CharField(max_length=6, choices=[('M', 'Male'), ('F', 'Female')])),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('skype', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
