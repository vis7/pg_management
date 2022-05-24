from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import CUser
from .forms import CUserCreationForm

# Create your views here.
class CUserCreationView(CreateView):
    model = CUser
    form_class = CUserCreationForm
    template_name = 'registration/signup.html'

class CUserDetailView(DetailView):
    model = CUser
    template_name = 'accounts/user_details.html'

def index(request):
    return render(request, 'index.html')
