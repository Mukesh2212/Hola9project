# Generated by Django 4.0.3 on 2023-11-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentbox', '0034_alter_adscomment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adscomment',
            name='date',
            field=models.CharField(default='2023-11-08', max_length=10),
        ),
    ]
