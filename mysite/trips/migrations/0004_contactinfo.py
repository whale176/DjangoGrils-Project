# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20151020_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('age', models.CharField(max_length=3)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
