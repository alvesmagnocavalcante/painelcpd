from django.urls import path
from . import views

urlpatterns = [
    path('', views.password_view, name='password_view'),
]
