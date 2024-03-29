# Generated by Django 4.1.3 on 2022-12-11 03:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0007_alter_packagesubscriptions_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagesubscriptions',
            name='activation_date',
            field=models.DateTimeField(verbose_name='Activation Date'),
        ),
        migrations.AlterField(
            model_name='packagesubscriptions',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 10, 8, 16, 22, 487944), verbose_name='Expirty Date'),
        ),
    ]
