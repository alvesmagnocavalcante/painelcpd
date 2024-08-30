from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_barcode, name='generate_barcode'),
]
