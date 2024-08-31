from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),  # Tela inicial (Painel de Utilitários)
    path('links/', include('links.urls')),  # App Links
    path('pdv-senhas/', include('pdv_senhas.urls')),  # App Senhas de PDV
    path('barcode/', include('barcode_generator.urls')),  # App Gerador de Código de Barras
    path('sitef-errors/', include('sitef_errors.urls')),  # App de Erros do Sitef
]

