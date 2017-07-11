# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('courses', '0003_auto_20170707_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(null=True, related_name='+', to='coaches.Coach'),
        ),
        migrations.AddField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(null=True, related_name='+', to='coaches.Coach'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='order',
            field=models.PositiveIntegerField(default=0, unique=False),
        ),
    ]
