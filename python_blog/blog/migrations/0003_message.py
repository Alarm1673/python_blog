# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150821_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('call_url', models.URLField(null=True, verbose_name=b'URL\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
            ],
            options={
                'verbose_name': '\u7559\u8a00',
                'verbose_name_plural': '\u7559\u8a00',
            },
        ),
    ]
