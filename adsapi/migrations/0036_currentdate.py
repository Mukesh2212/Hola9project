# Generated by Django 4.0.3 on 2022-12-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0035_pricing_orderid'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateFiled', models.CharField(max_length=1211)),
            ],
        ),
    ]
