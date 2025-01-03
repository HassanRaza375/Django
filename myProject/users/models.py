from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Role-based flag (admin or regular user)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
