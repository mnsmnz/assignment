# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 08:39
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chocolate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Chocolate Name')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Chocolate Description')),
                ('manufacturer', models.CharField(blank=True, max_length=100, verbose_name='Chocolate Manufacturer')),
                ('price', models.IntegerField(blank=True, help_text='4 digits maximum', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)], verbose_name='Chocolate Price')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_user',
        ),
        migrations.AlterUniqueTogether(
            name='courseenrollment',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='courseenrollment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='courseenrollment',
            name='order',
        ),
        migrations.RemoveField(
            model_name='courseenrollment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='coursemodules',
            name='course',
        ),
        migrations.RemoveField(
            model_name='courseprogress',
            name='checkout',
        ),
        migrations.RemoveField(
            model_name='courseprogress',
            name='module',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='CourseEnrollment',
        ),
        migrations.DeleteModel(
            name='CourseModules',
        ),
        migrations.DeleteModel(
            name='CourseProgress',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
