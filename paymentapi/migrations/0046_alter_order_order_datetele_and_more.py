# Generated by Django 4.0.3 on 2024-01-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentapi', '0045_alter_order_order_datetele_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_dateTele',
            field=models.CharField(default='2024-01-04', max_length=155),
        ),
        migrations.AlterField(
            model_name='transactiondetails',
            name='ordrDate',
            field=models.CharField(default='2024-01-04', max_length=155),
        ),
        migrations.AlterField(
            model_name='transationidone',
            name='date_created',
            field=models.CharField(default='2024-01-04', max_length=550),
        ),
    ]
