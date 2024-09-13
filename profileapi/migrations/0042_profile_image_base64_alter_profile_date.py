# Generated by Django 4.0.3 on 2023-12-29 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapi', '0041_alter_profile_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image_base64',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.CharField(default='2023-12-29', max_length=10),
        ),
    ]
