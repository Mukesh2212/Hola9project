# Generated by Django 4.0.3 on 2023-04-25 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paymentapi', '0016_transactiondetails_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_dateTele',
            field=models.CharField(default='2023-04-25', max_length=155),
        ),
        migrations.AlterField(
            model_name='transactiondetails',
            name='ordrDate',
            field=models.CharField(default='2023-04-25', max_length=155),
        ),
        migrations.AlterField(
            model_name='transationidone',
            name='date_created',
            field=models.CharField(default='2023-04-25', max_length=550),
        ),
        migrations.CreateModel(
            name='VerifiedCustomerMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('plan_type', models.CharField(blank=True, max_length=100, null=True)),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
