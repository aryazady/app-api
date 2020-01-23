from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, \
    PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extras):
        """create and save user"""
        if not email:
            raise ValueError('email validation failed')
        user = self.model(email=self.normalize_email(email), **extras)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extras):
        """create and save superuser"""
        superuser = self.create_user(email, password, **extras)
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save(using=self._db)

        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    """customize user model"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
