# Generated by Django 4.0.3 on 2022-12-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0039_product_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsmangeme',
            name='date_created',
            field=models.CharField(default='2022-12-29', max_length=20),
        ),
        migrations.AlterField(
            model_name='paymentdetailsvalues',
            name='date',
            field=models.CharField(default='2022-12-29', max_length=10),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='ads_timing',
            field=models.CharField(default='2022-12-29', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='realestateenquery',
            name='date_created',
            field=models.CharField(default='2022-12-29', max_length=150),
        ),
        migrations.AlterField(
            model_name='reportads',
            name='dates',
            field=models.CharField(default='2022-12-29', max_length=30),
        ),
    ]
