# Generated by Django 5.1.1 on 2024-09-07 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customer_addresse_alter_customer_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone2',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
