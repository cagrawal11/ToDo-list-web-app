# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ListApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TaskDescription', models.TextField()),
                ('TaskCreatedOn', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ListTask',
        ),
        migrations.DeleteModel(
            name='ToDOList',
        ),
    ]
