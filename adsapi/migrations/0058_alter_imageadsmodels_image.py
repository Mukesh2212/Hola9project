# Generated by Django 4.0.3 on 2023-07-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0057_alter_adsmangeme_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageadsmodels',
            name='image',
            field=models.CharField(blank=True, max_length=1502222222222222, null=True),
        ),
    ]
