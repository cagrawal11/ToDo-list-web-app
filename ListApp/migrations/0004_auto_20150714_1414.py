# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ListApp', '0003_addtask_taskauthor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtask',
            name='TaskCreatedOn',
            field=models.DateTimeField(),
        ),
    ]
