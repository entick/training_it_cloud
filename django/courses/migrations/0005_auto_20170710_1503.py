# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20170710_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(null=True, related_name='assistant_courses+', to='coaches.Coach'),
        ),
        migrations.AlterField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(null=True, related_name='coach_courses+', to='coaches.Coach'),
        ),
    ]
