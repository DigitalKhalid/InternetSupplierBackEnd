# Generated by Django 4.1.3 on 2022-12-04 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_customer_subarea'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='area',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='image',
        ),
    ]
