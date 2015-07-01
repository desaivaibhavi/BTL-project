# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='item_post',
            field=models.ForeignKey(related_name='item_post', default=b'', to='zapp.item'),
        ),
        migrations.AddField(
            model_name='post',
            name='specs_post',
            field=models.ForeignKey(related_name='specs_post', default=b'', to='zapp.specs'),
        ),
    ]
