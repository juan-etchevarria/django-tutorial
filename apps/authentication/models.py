from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Model User

    """

    class Meta:
        db_table = "auth_user"