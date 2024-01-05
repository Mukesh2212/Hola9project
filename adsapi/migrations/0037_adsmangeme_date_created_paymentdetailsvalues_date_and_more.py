# Generated by Django 4.0.3 on 2022-12-23 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0036_currentdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='adsmangeme',
            name='date_created',
            field=models.CharField(default='2022-12-23', max_length=20),
        ),
        migrations.AddField(
            model_name='paymentdetailsvalues',
            name='date',
            field=models.CharField(default='2022-12-23', max_length=10),
        ),
        migrations.AddField(
            model_name='pricing',
            name='ads_timing',
            field=models.CharField(default='2022-12-23', max_length=30),
        ),
        migrations.AddField(
            model_name='realestateenquery',
            name='date_created',
            field=models.CharField(default='2022-12-23', max_length=150),
        ),
        migrations.AddField(
            model_name='reportads',
            name='dates',
            field=models.CharField(default='2022-12-23', max_length=30),
        ),
    ]
