# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BTL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('BTL_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=300)),
                ('item_BTL', models.ForeignKey(related_name='iten_BTL', to='zapp.BTL')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lang_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instruct_post', models.CharField(max_length=2000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('qty_post', models.IntegerField(default=0)),
                ('BTLtype_post', models.ForeignKey(related_name='BTLtype_post', to='zapp.BTL')),
                ('city_post', models.ManyToManyField(to='zapp.City')),
                ('lang_post', models.ManyToManyField(to='zapp.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Rtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rtype_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='specs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specs_name', models.CharField(max_length=300)),
                ('specs_qty', models.IntegerField(default=0)),
                ('specs_item', models.ForeignKey(related_name='specs_item', to='zapp.item')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='rtype_post',
            field=models.ForeignKey(related_name='rtype_post', to='zapp.Rtype'),
        ),
    ]
