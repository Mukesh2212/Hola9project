# Generated by Django 4.0.3 on 2022-08-19 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0020_pricing_adsleft'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=2322)),
                ('password', models.CharField(max_length=2322)),
            ],
        ),
    ]
