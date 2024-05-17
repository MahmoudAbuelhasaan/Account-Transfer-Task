from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_list, name='account_list'),
    path('<int:pk>/', views.account_detail, name='account_detail'),
    path('transfer/', views.transfer_funds, name='transfer_funds'),
    path('upload/', views.upload_accounts, name='upload_accounts'),
]