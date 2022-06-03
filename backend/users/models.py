from email.policy import default
from inspect import modulesbyfile
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class User(AbstractUser):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(verbose_name=_("username"), max_length=255, unique=True)
    first_name = models.CharField(verbose_name=_("First name"), max_length=55)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=55)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD="email"

    REQUIRED_FIELDS=["username", "first_name", "last_name"]

    objects = CustomUserManager()


    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username.title()

    
    @property
    def get_fullname(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    
    def get_shortname(self):
        return self.username
