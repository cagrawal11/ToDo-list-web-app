# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ListApp', '0002_auto_20150708_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtask',
            name='TaskAuthor',
            field=models.CharField(default=b'Chetan', max_length=20),
        ),
    ]
