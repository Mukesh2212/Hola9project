# Generated by Django 4.0.3 on 2023-04-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0053_product_phonenumbercollectvisiters_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_expire',
            field=models.CharField(default='null', max_length=150),
        ),
    ]
