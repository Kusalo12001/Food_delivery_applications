# Generated by Django 5.0.2 on 2024-02-16 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0004_calculateprices_remove_item_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CalculatePrices',
        ),
    ]