# Generated by Django 4.1.3 on 2022-11-25 17:56

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='themedetail',
            name='border_color',
            field=colorfield.fields.ColorField(default='#FFFFFFFF', image_field=None, max_length=18, samples=None, verbose_name='Border Color'),
        ),
        migrations.AlterField(
            model_name='themedetail',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFFFF', image_field=None, max_length=18, samples=None, verbose_name='Text Color'),
        ),
        migrations.AlterField(
            model_name='themedetail',
            name='field_color',
            field=colorfield.fields.ColorField(default='#FFFFFFFF', image_field=None, max_length=18, samples=None, verbose_name='Field Text Color'),
        ),
    ]
