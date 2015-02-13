# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='skill',
            field=models.ForeignKey(to='cards.Skill', default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='problems',
            field=models.ManyToManyField(blank=True, null=True, to='cards.Problem'),
            preserve_default=True,
        ),
    ]
