# Generated by Django 4.1.3 on 2023-01-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_setting_bill_auto_print'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='connection_id_prefix',
            field=models.CharField(default='BizzSole', max_length=50, verbose_name='Connection ID Prefix'),
        ),
        migrations.AddField(
            model_name='setting',
            name='order_id_prefix',
            field=models.CharField(default='BizzSole', max_length=50, verbose_name='Order ID Prefix'),
        ),
    ]
