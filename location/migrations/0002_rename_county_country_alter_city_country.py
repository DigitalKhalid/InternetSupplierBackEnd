# Generated by Django 4.1.3 on 2022-11-26 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='County',
            new_name='Country',
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='location.country', verbose_name='Country'),
        ),
    ]
