# Generated by Django 4.1.3 on 2022-12-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0018_alter_connection_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive', max_length=20, verbose_name='Status'),
        ),
    ]