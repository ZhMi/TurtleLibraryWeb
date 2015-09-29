# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookManage', '0002_auto_20150926_1236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='borrowrecords',
            options={'ordering': ['borrow_start_time'], 'verbose_name': '\u501f\u9605\u8bb0\u5f55', 'verbose_name_plural': '\u501f\u9605\u8bb0\u5f55'},
        ),
    ]
