# Generated by Django 4.0.3 on 2023-04-20 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0047_pricing_validity_alter_adsmangeme_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsmangeme',
            name='date_created',
            field=models.CharField(default='2023-04-20', max_length=20),
        ),
        migrations.AlterField(
            model_name='paymentdetailsvalues',
            name='date',
            field=models.CharField(default='2023-04-20', max_length=10),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='ads_timing',
            field=models.CharField(default='2023-04-20', max_length=30),
        ),
        migrations.AlterField(
            model_name='realestateenquery',
            name='date_created',
            field=models.CharField(default='2023-04-20', max_length=150),
        ),
        migrations.AlterField(
            model_name='reportads',
            name='dates',
            field=models.CharField(default='2023-04-20', max_length=30),
        ),
    ]
