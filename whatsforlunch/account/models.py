from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_superuser(self, username, password, **extra_fields):
        user = self.model(email=username, is_staff=True, is_active=True, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):

    class Meta:
        db_table = 'user'
