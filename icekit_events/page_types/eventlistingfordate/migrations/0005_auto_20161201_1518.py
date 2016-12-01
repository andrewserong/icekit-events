# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventlistingfordate', '0004_auto_20161115_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlistingpage',
            name='hero_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True, help_text=b'The hero image for this content.', to='icekit_plugins_image.Image', null=True),
        ),
    ]
