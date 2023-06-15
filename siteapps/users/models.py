import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from rest_framework.authtoken.models import Token

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def get_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_admin = True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    public_id      = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True, editable=False)
    email          = models.EmailField(verbose_name='Email Address', max_length=60, unique=True)
    first_name     = models.CharField(verbose_name='First Name', max_length=60, blank=True)
    last_name      = models.CharField(verbose_name='Last Name', max_length=60, blank=True)
    username       = models.CharField(max_length=30, unique=True)
    is_admin       = models.BooleanField(default=False)
    is_staff       = models.BooleanField(default=False)
    is_superuser   = models.BooleanField(default=False)
    is_active      = models.BooleanField(default=True)
    created        = models.DateTimeField(auto_now_add=True)
    edited         = models.BooleanField(default=False)
    updated        = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def __str__(self) -> str:
        return self.username


# all I know for now is that these are required fields
# else the admin page would not load
    # def has_perm(self, perm, obj=None):
    #     return self.is_admin
    # def has_module_perms(self, app_label):
    #     return True

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
