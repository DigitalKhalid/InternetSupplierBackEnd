# Generated by Django 4.1.3 on 2022-12-04 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_rename_county_country_alter_city_country'),
        ('connection', '0010_connection_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='subarea',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='connections', to='location.subarea', verbose_name='Sub Area'),
            preserve_default=False,
        ),
    ]
