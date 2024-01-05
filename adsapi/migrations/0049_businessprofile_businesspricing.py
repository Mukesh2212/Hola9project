# Generated by Django 4.0.3 on 2023-04-20 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adsapi', '0048_alter_adsmangeme_date_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('company_name', models.CharField(max_length=100)),
                ('aadhar_card', models.ImageField(upload_to='')),
                ('pan_card', models.ImageField(upload_to='')),
                ('company_document', models.FileField(upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderID', models.CharField(max_length=1211, null=True)),
                ('category', models.CharField(max_length=2322, null=True)),
                ('validity', models.CharField(max_length=2322, null=True)),
                ('city', models.CharField(max_length=2322, null=True)),
                ('visiblity', models.CharField(max_length=2322, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
