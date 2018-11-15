from django.urls import path
from . import views

urlpatterns=[
    path(r'register', views.UserCreate.as_view(), name='account-create'),
]
