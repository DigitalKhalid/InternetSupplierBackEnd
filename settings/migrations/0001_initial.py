# Generated by Django 4.1.3 on 2022-12-28 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renew_order_before', models.IntegerField(default=5, verbose_name='Renew Order Before (Days)')),
            ],
        ),
    ]