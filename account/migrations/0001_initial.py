# Generated by Django 4.0.3 on 2024-04-30 13:49

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('name', models.CharField(max_length=200)),
                ('tc', models.BooleanField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.CharField(default=datetime.date.today, max_length=150)),
                ('phoneNumber', models.CharField(default=False, max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('auth_provider', models.CharField(default='email', max_length=255)),
                ('total_ads_posted', models.PositiveIntegerField(default=0)),
                ('active_devices', models.PositiveIntegerField(default=0)),
                ('token_key', models.CharField(blank=True, max_length=40, null=True, unique=True)),
                ('token_expiration_time', models.DurationField(default=datetime.timedelta(seconds=1))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('resume', models.FileField(default='null', upload_to='resumes/')),
                ('posted_by', models.CharField(default='null', max_length=100)),
                ('percentage', models.CharField(default='', max_length=200)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('jobtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('ads_id', models.CharField(blank=True, max_length=255, null=True)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('resume_base64', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=300)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('add_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=17)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('Introduction', models.CharField(blank=True, max_length=255, null=True)),
                ('filename', models.FileField(blank=True, max_length=255, null=True, upload_to='')),
                ('created_at', models.CharField(default='2024-04-30', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='JobsRequired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=200)),
                ('no_of_openings', models.IntegerField(default=None, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('job_responsiblity', models.CharField(max_length=200)),
                ('technical_skills', models.CharField(max_length=200)),
                ('Preferred_qualification', models.CharField(max_length=200, null=True)),
                ('education', models.CharField(max_length=200, null=True)),
                ('created_at', models.CharField(default='2024-04-30', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format +919999999999. Up to 14 digits allowed.', regex='^\\+?1?\\d{9,10}$')])),
                ('otp', models.CharField(blank=True, max_length=9, null=True)),
                ('count', models.IntegerField(default=0, help_text='Number of otp_sent')),
                ('validated', models.BooleanField(default=False, help_text='If it is true, that means user have validate otp correctly in second API')),
                ('otp_session_id', models.CharField(default='', max_length=120, null=True)),
                ('username', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('email', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('password', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('profile', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(null=True, upload_to='upload/images')),
                ('created_at', models.CharField(default='2024-04-30', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='TelemetryDaa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(blank=True, max_length=255, null=True)),
                ('teleId', models.IntegerField(default=None, null=True)),
                ('date', models.CharField(default='2024-04-30', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserLoginTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('previous_login_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
