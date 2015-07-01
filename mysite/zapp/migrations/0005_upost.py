# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zapp', '0004_auto_20150701_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_upost', models.CharField(default=b'', max_length=2000)),
                ('status_upost', models.IntegerField(default=0)),
                ('post_upost', models.ForeignKey(related_name='post_upost', default=b'', to='zapp.Post')),
            ],
        ),
    ]
