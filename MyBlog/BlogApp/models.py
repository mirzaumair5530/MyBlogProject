from django.db import models
import datetime
from secrets import token_hex
import os
from django.contrib.auth.models import UserManager, AbstractUser


# Create your models here.
def postid():
    return 'Post' + token_hex(5)


def upload_to(_, filename):
    ext = filename.split('0')[-1]
    return "{0}.{1}".format(token_hex(4), ext)








class RegisteredUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Email Field is required.')
        if not username:
            raise ValueError('Username Field is required.')

        user = self.model(
            email=self.normalize_email(email),
            username=username,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, username, email=None, password=None, **extra_fields):

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)




class RegisterUser(AbstractUser):
    email = models.EmailField(primary_key=True, unique=True, verbose_name='email')
    username = models.CharField(unique=True, verbose_name='username', max_length=30)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_joined = models.DateTimeField(verbose_name='Joined Date', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)
    profileImage = models.ImageField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    objects = RegisteredUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def default_admin(self):
        admin = self.objects.filter(is_admin=True).first()
        return admin


class BlogPost(models.Model):
    postID = models.CharField(primary_key=True, max_length=200, default=postid)
    postHeader = models.TextField(null=True)
    postData = models.TextField(null=True)
    postDate = models.DateField(auto_now=True)
    postImage = models.ImageField(upload_to=upload_to)
    postAdmin = models.ForeignKey( to=RegisterUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.postID