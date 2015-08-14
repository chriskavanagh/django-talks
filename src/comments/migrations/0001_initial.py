# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=1024)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('talk', models.ManyToManyField(related_name='comments', to='talks.TalkList')),
            ],
        ),
    ]
