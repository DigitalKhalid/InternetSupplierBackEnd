# Generated by Django 4.1.3 on 2022-12-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=20, verbose_name='Type'),
        ),
    ]
