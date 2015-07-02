# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zapp', '0005_upost'),
    ]

    operations = [
        migrations.CreateModel(
            name='specs_order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specs_1', models.BooleanField(default=False)),
                ('specs_2', models.BooleanField(default=False)),
                ('specs_3', models.BooleanField(default=False)),
                ('specs_4', models.BooleanField(default=False)),
                ('specs_5', models.BooleanField(default=False)),
                ('specs_6', models.BooleanField(default=False)),
                ('specs_7', models.BooleanField(default=False)),
                ('specs_8', models.BooleanField(default=False)),
                ('specs_9', models.BooleanField(default=False)),
                ('specs_10', models.BooleanField(default=False)),
                ('specs_11', models.BooleanField(default=False)),
                ('specs_12', models.BooleanField(default=False)),
                ('specs_13', models.BooleanField(default=False)),
                ('specs_14', models.BooleanField(default=False)),
                ('specs_15', models.BooleanField(default=False)),
                ('specs_16', models.BooleanField(default=False)),
                ('specs_17', models.BooleanField(default=False)),
                ('specs_18', models.BooleanField(default=False)),
                ('specs_1_qty', models.IntegerField(default=0)),
                ('specs_2_qty', models.IntegerField(default=0)),
                ('specs_3_qty', models.IntegerField(default=0)),
                ('specs_4_qty', models.IntegerField(default=0)),
                ('specs_5_qty', models.IntegerField(default=0)),
                ('specs_6_qty', models.IntegerField(default=0)),
                ('specs_7_qty', models.IntegerField(default=0)),
                ('specs_8_qty', models.IntegerField(default=0)),
                ('specs_9_qty', models.IntegerField(default=0)),
                ('specs_10_qty', models.IntegerField(default=0)),
                ('specs_11_qty', models.IntegerField(default=0)),
                ('specs_12_qty', models.IntegerField(default=0)),
                ('specs_13_qty', models.IntegerField(default=0)),
                ('specs_14_qty', models.IntegerField(default=0)),
                ('specs_15_qty', models.IntegerField(default=0)),
                ('specs_16_qty', models.IntegerField(default=0)),
                ('specs_17_qty', models.IntegerField(default=0)),
                ('specs_18_qty', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='qty_post',
        ),
        migrations.AlterField(
            model_name='post',
            name='specs_post',
            field=models.ForeignKey(related_name='specs_post', default=b'', to='zapp.specs_order'),
        ),
    ]
