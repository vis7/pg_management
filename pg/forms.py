from django import forms
from .models import Issue
from accounts.models import CUser

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['name', 'description']

    # def form_valid(self, form):
    #     form = form.save(commit=False)
    #     form.raised_by = CUser.objects.get(pk=1) # self.request.user
    #     form.save()
    #     return super().form_valid(form)

    def save(self):
        instance = super(IssueForm, self).save(commit=False)
        instance.raised_by = CUser.objects.get(pk=1)
        instance.save()
        return instance
