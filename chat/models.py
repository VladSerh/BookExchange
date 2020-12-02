from django.db import models
from django.contrib.auth import models as auth

from offers.models import Offers


class Messages(models.Model):
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
    sender = models.ForeignKey(auth.User, on_delete=models.CASCADE)
