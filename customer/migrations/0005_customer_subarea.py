# Generated by Django 4.1.3 on 2022-12-04 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_rename_county_country_alter_city_country'),
        ('customer', '0004_rename_steet_address_customer_street_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='subarea',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='location.subarea', verbose_name='Sub Area'),
            preserve_default=False,
        ),
    ]
