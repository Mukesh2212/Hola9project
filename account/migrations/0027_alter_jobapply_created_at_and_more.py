# Generated by Django 4.2.1 on 2023-07-12 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_alter_jobapply_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapply',
            name='created_at',
            field=models.CharField(default='2023-07-12', max_length=150),
        ),
        migrations.AlterField(
            model_name='jobsrequired',
            name='created_at',
            field=models.CharField(default='2023-07-12', max_length=150),
        ),
        migrations.AlterField(
            model_name='reviewsection',
            name='created_at',
            field=models.CharField(default='2023-07-12', max_length=150),
        ),
        migrations.AlterField(
            model_name='telemetrydaa',
            name='date',
            field=models.CharField(default='2023-07-12', max_length=10),
        ),
    ]
