from django.urls import path
from . import views
from dashboard.views import dashboard_view

urlpatterns = [
    path('registro/', views.registro_balanca, name='registro_balanca'),
    path('lista/', views.lista_balanca, name='lista_balanca'),
    path('exportar/', views.exportar_balanca_xlsx, name='exportar_balanca_xlsx'),
    path('editar/<int:pk>/', views.editar_balanca, name='editar_balanca'),
    path('excluir/<int:pk>/', views.excluir_balanca, name='excluir_balanca'),
    path('', dashboard_view, name='dashboard_index'),
]
    