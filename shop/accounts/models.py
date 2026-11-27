from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Tier(models.TextChoices):
        STANDARD = "standard"
        SILVER = "silver"
        GOLD = "gold"

    email = models.EmailField(unique=True)
    loyalty_tier = models.CharField(max_length=10, choices=Tier.choices, default=Tier.STANDARD)
