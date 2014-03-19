import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


def avatar_upload_to(instance, filename):
    if filename.split(os.sep):
        ext = '.' + filename.split(os.sep)[-1].split('.')[-1]
        filename = str(instance.full_name).replace(' ', '_') + str(instance.id) + ext
    return os.sep.join(['avatars', str(instance.id), filename])


class UserManager(BaseUserManager):

    def create_superuser(self, username, password, **extra_fields):
        user = self.model(email=username, is_staff=True, is_active=True, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):

    email           = models.CharField(max_length=254, unique=True)
    username        = models.CharField(max_length=100)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    date_joined     = models.DateTimeField(auto_now_add=True)
    avatar          = models.FileField(upload_to=avatar_upload_to, null=True, blank=True, max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'user'
