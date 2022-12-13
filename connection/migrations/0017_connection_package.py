# Generated by Django 4.1.3 on 2022-12-10 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_product_purchase_price_and_more'),
        ('connection', '0016_remove_connection_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='package',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='connections', to='product.product', verbose_name='Package'),
        ),
    ]