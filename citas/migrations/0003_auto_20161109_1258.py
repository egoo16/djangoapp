# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('citas', '0002_auto_20161106_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='fecha_nacimiento',
        ),
        migrations.AddField(
            model_name='cita',
            name='autor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cita',
            name='fecha',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cita',
            name='hora',
            field=models.CharField(null=True, max_length=25),
        ),
    ]
