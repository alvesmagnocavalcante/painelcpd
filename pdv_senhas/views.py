from django.shortcuts import render
from datetime import datetime
from django.core.cache import cache

def calculate_password(pdv_number):
    today = datetime.now()
    # Concatenar dia e mês sem zero à esquerda
    day_str = str(today.day)
    month_str = str(today.month)
    day_month = int(day_str + month_str)
    password_number = day_month + pdv_number
    password = f"pdv@{password_number}"
    return password

def password_view(request):
    pdv_number = request.GET.get('pdv_number')
    password = None

    if pdv_number:
        try:
            pdv_number = int(pdv_number)

            # Gerar a chave do cache com base no número do PDV e na data atual
            cache_key = f"pdv_password_{pdv_number}_{datetime.now().strftime('%Y%m%d')}"

            # Tentar pegar a senha do cache
            password = cache.get(cache_key)

            # Se a senha não estiver no cache, gerar e armazenar no cache
            if not password:
                password = calculate_password(pdv_number)
                cache.set(cache_key, password, 86400)  # Cache por 24 horas

        except ValueError:
            password = "Número de PDV inválido. Por favor, forneça um número válido."

    else:
        password = "Por favor, forneça o número do PDV."

    return render(request, 'pdv_password.html', {'password': password, 'pdv_number': pdv_number})
