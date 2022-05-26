from django.urls import path
from .views import IssueCreate, IssueUpdate, IssueDelete, IssueDetail, IssueList

app_lable = 'pg'

urlpatterns = [
    path('issue/create', IssueCreate.as_view(), name='issue_create'),
    path('issue/<int:pk>', IssueDetail.as_view(), name='issue_detail'),
    path('issue/<int:pk>/update', IssueUpdate.as_view(), name='issue_update'),
    path('issue/<int:pk>/delete', IssueDelete.as_view(), name='issue_delete'),
    path('issue/', IssueList.as_view(), name='issue_list')
]

