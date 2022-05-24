from pyexpat import model
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class CUser(AbstractUser):
    mobile = PhoneNumberField(null=True, blank=True, unique=True)
    date_joined = models.DateField(auto_now_add=True)
    is_manager = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

