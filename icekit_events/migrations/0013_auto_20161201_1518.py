# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import timezone.timezone
import icekit.fields


class Migration(migrations.Migration):

    dependencies = [
        ('icekit_events', '0012_occurrence_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='OccurrenceUrlPrefix',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(db_index=True, default=timezone.timezone.now, editable=False)),
                ('modified', models.DateTimeField(db_index=True, default=timezone.timezone.now, editable=False)),
                ('name', models.TextField(unique=True, blank=True, help_text=b'Name of the URL to use for occurrences.')),
                ('url', models.URLField(help_text=b'URL to use for each occurrence for an event.')),
            ],
            options={
                'abstract': False,
                'get_latest_by': 'pk',
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='eventbase',
            name='occurrence_append_external_ref',
            field=models.BooleanField(default=True, help_text='Append occurrence external_ref to each occurrence URL.'),
        ),
        migrations.AddField(
            model_name='eventbase',
            name='occurrence_url',
            field=icekit.fields.ICEkitURLField(max_length=300, help_text='The URL to use for each occurrence.', null=True, verbose_name='Occurrence URL', blank=True),
        ),
    ]
