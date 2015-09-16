# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_spec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_n', models.IntegerField()),
                ('product_type', models.CharField(max_length=55)),
                ('product_name', models.CharField(max_length=55)),
                ('product_code', models.CharField(max_length=15)),
                ('price', models.IntegerField()),
                ('stock_count', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('Update_date', models.DateTimeField()),
            ],
        ),
    ]
