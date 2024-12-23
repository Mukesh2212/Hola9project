from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from account.models import User
# * Custom Account Manger


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, contact_number, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff = True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser = True')

        return self.create_user(email, user_name, password, contact_number, **other_fields)

    def create_user(self, email, user_name, password, contact_number, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          contact_number=contact_number, **other_fields)
        user.set_password(password)
        user.save()
        return user

# * Custom User


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    contact_number = models.IntegerField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', 'contact_number']

    def __str__(self):
        return self.user_name

import datetime
# * Table that stores the OTP and is verfied or not
class OTPVerifiaction(models.Model):
    phone_number = models.IntegerField()
    otp = models.CharField(max_length=4)
    is_verfied = models.BooleanField(default=False)
    date = models.CharField(max_length=10,blank=False ,default=datetime.datetime.now().strftime('%Y-%m-%d'))

class PhoneUser(models.Model):
    phone_number=models.IntegerField()
    user= models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    date = models.CharField(max_length=10,blank=False ,default=datetime.datetime.now().strftime('%Y-%m-%d'))


