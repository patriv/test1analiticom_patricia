from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# 
# class MyUserManager(BaseUserManager):
#     def create_user(self, email, first_name,last_name, password):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             first_name=first_name,
#             last_name = last_name
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#
# class MyUser(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     first_name = models.CharField(max_length=35)
#     last_name = models.CharField(max_length=35)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#
#     objects = MyUserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['password']
