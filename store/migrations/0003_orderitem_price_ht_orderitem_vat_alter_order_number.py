# Generated by Django 5.1.1 on 2024-09-10 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price_ht',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='vat',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.CharField(blank=True, max_length=256, unique=True),
        ),
    ]