from django.urls import path
from .views import(
UserCreate,
UserLoginAPIView
)

urlpatterns=[
    path(r'register', UserCreate.as_view(), name='register'),
    path(r'login', UserLoginAPIView.as_view(), name='login'),

]
