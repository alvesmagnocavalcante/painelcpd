from django.urls import path
from .views import links_list

urlpatterns = [
    path('', links_list, name='links_list'),
]
