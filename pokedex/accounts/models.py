from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class ControleOTP(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(blank=False, null=False)
    codigo = models.CharField(max_length=6, blank=False, null=False) 


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(blank=False, null=False)
    codigo = models.CharField(max_length=6, blank=False, null=False)