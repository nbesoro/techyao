# Generated by Django 5.1.1 on 2024-09-11 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_orderitem_price_ht_orderitem_vat_alter_order_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="price_ttc",
            field=models.FloatField(default=0),
        ),
    ]
