# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('from_email', models.EmailField(max_length=254)),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]
