
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):

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

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email          = models.EmailField(verbose_name='Email Address', max_length=60, unique=True)
    first_name     = models.CharField(verbose_name='First Name', max_length=60, blank=True)
    last_name      = models.CharField(verbose_name='Last Name', max_length=60, blank=True)
    username       = models.CharField(max_length=30, unique=True)
    created        = models.DateTimeField(auto_now=True)
    is_admin       = models.BooleanField(default=False)
    is_staff       = models.BooleanField(default=False)
    is_superuser   = models.BooleanField(default=False)
    is_active      = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# all I know for now is that these are required fields
# else the admin page would not load
    # def has_perm(self, perm, obj=None):
    #     return self.is_admin
    # def has_module_perms(self, app_label):
    #     return True
