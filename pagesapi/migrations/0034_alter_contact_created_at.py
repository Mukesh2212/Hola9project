# Generated by Django 4.0.3 on 2023-11-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagesapi', '0033_alter_contact_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.CharField(default='2023-11-08', max_length=150),
        ),
    ]