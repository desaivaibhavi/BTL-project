# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zapp', '0003_post_email_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='BTLtype_post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='item_post',
        ),
    ]
