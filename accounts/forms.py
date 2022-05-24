from email.policy import default
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from django.db import transaction
from django import forms
from .models import CUser


class CUserCreationForm(UserCreationForm):
    mobile = PhoneNumberField()
    # date_joined = forms.DateField(required=False)
    is_manager = forms.BooleanField(required=False)
    is_member = forms.BooleanField(required=False)

    class Meta(UserCreationForm.Meta):
        model = CUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.mobile = self.cleaned_data.get('mobile')
        # user.date_joined = self.cleaned_data.get('date_joined')
        user.is_manager = self.cleaned_data.get('is_manager')
        user.is_member = self.cleaned_data.get('is_member')
        user.save()
        return user
