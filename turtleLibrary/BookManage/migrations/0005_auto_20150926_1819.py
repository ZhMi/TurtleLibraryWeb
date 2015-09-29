# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookManage', '0004_auto_20150926_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username'], 'verbose_name': '\u8bfb\u8005', 'verbose_name_plural': '\u8bfb\u8005'},
        ),
    ]
