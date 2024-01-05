# Generated by Django 4.0.3 on 2023-09-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0057_alter_adsmangeme_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesspricing',
            name='chatSupport',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='businesspricing',
            name='dedicatedRm',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='businesspricing',
            name='hol9Website',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='businesspricing',
            name='teleSupport',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='company_document_type',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='user_type',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='qrcode',
            name='token',
            field=models.CharField(default='null', max_length=36),
        ),
        migrations.AlterField(
            model_name='adsmangeme',
            name='date_created',
            field=models.CharField(default='2023-09-26', max_length=20),
        ),
        migrations.AlterField(
            model_name='imageadsmodels',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paymentdetailsvalues',
            name='date',
            field=models.CharField(default='2023-09-26', max_length=10),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='ads_timing',
            field=models.CharField(default='2023-09-26', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='City',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='PlanCategory',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='adsType',
            field=models.CharField(default='null', max_length=232333332, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ads_limit',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ads_timing',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='college',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='colorCheck',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='end',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='engine',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='extraField',
            field=models.CharField(default='null', max_length=232333332, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='featured_ads',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='kmdriven',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='locality',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='oldPetsCheck',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='phoneNumberCollectVisiters',
            field=models.CharField(default='null', max_length=123123, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='plan',
            field=models.CharField(default='null', max_length=232333332, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='registrationYear',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='school',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='setkmDriven',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='setregistrationYear',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizeCheck',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='start',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='state',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='support',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='top_listing',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.CharField(default='null', max_length=123123, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='year',
            field=models.CharField(default='null', max_length=2322, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='zip_code',
            field=models.CharField(default='null', max_length=6),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='image',
            field=models.CharField(blank=True, default='NoData', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='realestateenquery',
            name='date_created',
            field=models.CharField(default='2023-09-26', max_length=150),
        ),
        migrations.AlterField(
            model_name='reportads',
            name='dates',
            field=models.CharField(default='2023-09-26', max_length=30),
        ),
    ]
