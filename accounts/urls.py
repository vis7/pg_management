from django.urls import path
from .views import CUserCreationView, CUserDetailView

app_lable = 'accounts'

urlpatterns = [
    path('signup', CUserCreationView.as_view(), name='signup'),
    path('user/<int:pk>', CUserDetailView.as_view(), name='user_detail')
]

