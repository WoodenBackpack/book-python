# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ['country', '-city'], 'verbose_name': 'Address', 'verbose_name_plural': 'Adresses'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['name'], 'verbose_name': 'Document', 'verbose_name_plural': 'Documents'},
        ),
        migrations.AddField(
            model_name='contact',
            name='photo',
            field=models.FileField(default=None, null=True, upload_to='', verbose_name='Photo'),
            preserve_default=False,
        ),
    ]
