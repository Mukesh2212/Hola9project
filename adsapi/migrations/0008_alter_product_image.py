# Generated by Django 4.0.3 on 2022-07-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, max_length=1502222222222222, null=True),
        ),
    ]