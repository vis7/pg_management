from django.shortcuts import render
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView, ListView
)
from .forms import IssueForm
from .models import Issue

# Create your views here.
class IssueCreate(CreateView):
    form_class = IssueForm
    template_name = 'pg/issue_create.html'

class IssueDetail(DetailView):
    model = Issue
    template_name = 'pg/issue_detail.html'

class IssueUpdate(UpdateView):
    form_class = 'pg/issue_update.html'

class IssueDelete(DeleteView):
    model = Issue
    template_name = 'pg/issue_delete.html'

class IssueList(ListView):
    queryset = Issue.objects.all()
    template_name = 'pg/issue_list.html'
