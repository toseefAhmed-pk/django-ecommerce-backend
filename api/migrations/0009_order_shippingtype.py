# Generated by Django 3.0.5 on 2021-06-02 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210516_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shippingType',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
