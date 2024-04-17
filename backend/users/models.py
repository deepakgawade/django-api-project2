
import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)
from django.utils import timezone
 

# Create your models here.

class MyUserManager(BaseUserManager):


    def create_user(self, email, date_of_birth, password= None):
        """
        creates and saves a new user with given email, date of birth and password

        """
        if not email:
            raise ValueError('User must have an email address')
        
        user= self.model(email=self.normalize_email(email),date_of_birth=date_of_birth,)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email,date_of_birth, password=None):
         """
         Creates and saves a superuser
         """
         user=self.create_user(email,password=password,date_of_birth=date_of_birth)
         user.is_admin=True
         user.save(using=self._db)
         return user
    
        
class MyUser(AbstractBaseUser):
    email= models.EmailField(max_length=255,unique=True)
    date_of_birth=models.DateField()
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    credits=models.PositiveIntegerField(default=100)
    linkedin_token=models.TextField(blank=True,default='')
    expiry_date=models.DateTimeField(null=True,blank=True)
    objects=MyUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['date_of_birth']

    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_out_of_credits(self):
        return self.credits>0
    @property
    def has_sufficient_credit(self,cost):
        return self.credits-cost>=0
    @property
    def linkedin_signed_in(self):
        return bool(self.linkedin_token) and self.expiry_date>timezone.now()

