# Generated by Django 4.0.3 on 2023-08-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0060_businessprofile_company_document_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='token',
            field=models.CharField(default='null', max_length=36),
        ),
    ]
