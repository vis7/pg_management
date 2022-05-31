from django.db import models
from django.urls import reverse
from accounts.models import CUser

ISSUE_TYPE = [
    ('PERSONAL', 'personal'),
    ('ROOM', 'room'),
    ('GENERAL', 'general')
]

# Create your models here.
class Issue(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    issue_type = models.CharField(max_length=10, choices=ISSUE_TYPE)
    raised_by = models.ForeignKey(CUser, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("issue_detail", kwargs={"pk": self.pk})
