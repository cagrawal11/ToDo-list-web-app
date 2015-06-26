# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListTask',
            fields=[
                ('Task_Id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('Description', models.TextField()),
                ('Created', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ToDOList',
            fields=[
                ('List_Id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('List_name', models.CharField(default=b'', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
