# Generated by Django 4.0.3 on 2022-08-18 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adsapi', '0018_alter_qrcode_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PlanCategory',
            field=models.CharField(max_length=2322, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='ads_limit',
            field=models.CharField(max_length=2322, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='ads_timing',
            field=models.CharField(max_length=2322, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='featured_ads',
            field=models.CharField(max_length=2322, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='support',
            field=models.CharField(max_length=2322, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='top_listing',
            field=models.CharField(max_length=2322, null=True),
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=2322)),
                ('featured_ads', models.CharField(max_length=2322)),
                ('ads_limit', models.CharField(max_length=2322)),
                ('ads_timing', models.CharField(max_length=2322)),
                ('top_listing', models.CharField(max_length=2322)),
                ('support', models.CharField(max_length=2322)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
