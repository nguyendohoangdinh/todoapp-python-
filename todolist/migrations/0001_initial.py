# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-20 07:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default=b'2019-03-20')),
                ('due_date', models.DateField(default=b'2019-03-20')),
                ('category', models.ForeignKey(default='general', on_delete=django.db.models.deletion.CASCADE, to='todolist.Category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
