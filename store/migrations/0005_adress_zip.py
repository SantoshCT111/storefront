# Generated by Django 4.2.1 on 2023-06-02 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_unit_price_product_one_unit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='adress',
            name='zip',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
