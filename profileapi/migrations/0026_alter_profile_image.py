# Generated by Django 4.0.3 on 2023-09-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapi', '0025_alter_profile_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='null', upload_to='upload/images'),
        ),
    ]