# Generated by Django 3.0.5 on 2021-06-03 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_order_shippingtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paidAt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]