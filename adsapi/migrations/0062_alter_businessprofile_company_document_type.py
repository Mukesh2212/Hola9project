# Generated by Django 4.0.3 on 2023-08-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0061_qrcode_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='company_document_type',
            field=models.TextField(default='null'),
        ),
    ]