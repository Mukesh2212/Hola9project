# Generated by Django 4.0.3 on 2024-04-30 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentbox', '0043_alter_adscomment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adscomment',
            name='date',
            field=models.CharField(default='2024-04-30', max_length=10),
        ),
    ]
