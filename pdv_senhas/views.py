from django.shortcuts import render
from datetime import datetime
from django.core.cache import cache

def calculate_password(pdv_number):
    today = datetime.now()
    day_month = int(f"{today.day}{today.month}")
    password_number = day_month + pdv_number
    password = f"pdv@{password_number}"
    return password

def password_view(request):
    pdv_number = request.GET.get('pdv_number')
    password = None

    if pdv_number:
        try:
            pdv_number = int(pdv_number)
            cache_key = f"pdv_password_{pdv_number}_{datetime.now().strftime('%Y%m%d')}"
            password = cache.get(cache_key)

            if not password:
                password = calculate_password(pdv_number)
                cache.set(cache_key, password, 86400)  # Cache por 24 horas

        except ValueError:
            password = "Número de PDV inválido"

    return render(request, 'pdv_password.html', {'password': password, 'pdv_number': pdv_number})
