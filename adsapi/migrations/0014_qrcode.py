# Generated by Django 4.0.3 on 2022-08-02 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0013_lastlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='QrCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=23222)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adsapi.product')),
            ],
        ),
    ]
