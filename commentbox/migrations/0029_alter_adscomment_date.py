# Generated by Django 4.0.3 on 2023-10-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentbox', '0028_alter_adscomment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adscomment',
            name='date',
            field=models.CharField(default='2023-10-09', max_length=10),
        ),
    ]