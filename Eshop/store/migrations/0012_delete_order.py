# Generated by Django 4.0.3 on 2022-08-22 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_order_address_alter_order_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]