# Generated by Django 4.1.3 on 2022-12-12 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_order_id_order_status_order_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Connection',
            new_name='connection',
        ),
    ]
