# Generated by Django 4.1.3 on 2022-11-26 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0005_connection_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connection',
            name='customer',
        ),
    ]
