# Generated by Django 4.0.3 on 2023-08-21 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapi', '0020_alter_profile_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.CharField(default='2023-08-21', max_length=10),
        ),
    ]
