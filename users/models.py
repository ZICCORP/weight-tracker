from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from datetime import datetime

#AbstractUser.
#gender options 
gender_choices = (
    ('m','Male'),
    ('f','Female'),
)



class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email=self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        return self._create_user(email,password,**extra_fields)

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Speruser must have is_superuser=True.")
        return self._create_user(email,password,**extra_fields)

class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=300,null=False,blank=False)
    last_name = models.CharField(max_length=300,null=False,blank=False)
    email = models.EmailField('email address',unique=True)
    birth_date = models.DateField(blank=False,null=False,default=datetime.today)
    gender = models.CharField(max_length=1, choices=gender_choices,blank=False,null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birth_date','gender','first_name','last_name']
    objects=UserManager()