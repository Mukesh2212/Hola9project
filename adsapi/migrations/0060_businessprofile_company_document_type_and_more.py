# Generated by Django 4.0.3 on 2023-08-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0059_businesspricing_chatsupport_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='company_document_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
