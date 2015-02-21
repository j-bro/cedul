# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cedul_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='email',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
