# Generated by Django 4.0.3 on 2022-10-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0026_product_kmdriven_product_registrationyear_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='extraField',
            field=models.CharField(max_length=232333332, null=True),
        ),
    ]
