# Generated by Django 4.0.3 on 2024-01-08 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_reg', '0042_alter_otpverifiaction_date_alter_phoneuser_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpverifiaction',
            name='date',
            field=models.CharField(default='2024-01-08', max_length=10),
        ),
        migrations.AlterField(
            model_name='phoneuser',
            name='date',
            field=models.CharField(default='2024-01-08', max_length=10),
        ),
    ]
