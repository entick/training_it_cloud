# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20170710_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(blank=True, null=True, related_name='assistant_courses+', to='coaches.Coach'),
        ),
        migrations.AlterField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, related_name='coach_courses+', to='coaches.Coach'),
        ),
    ]
