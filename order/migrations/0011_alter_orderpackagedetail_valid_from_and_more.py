# Generated by Django 4.1.3 on 2023-01-01 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_alter_orderpackagedetail_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderpackagedetail',
            name='valid_from',
            field=models.DateField(blank=True, null=True, verbose_name='Valid From'),
        ),
        migrations.AlterField(
            model_name='orderpackagedetail',
            name='valid_to',
            field=models.DateField(blank=True, null=True, verbose_name='Valid To'),
        ),
    ]
