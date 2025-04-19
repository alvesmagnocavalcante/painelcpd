from django.shortcuts import render
from datetime import datetime
from django.core.cache import cache

def calculate_password(pdv_number):
    today = datetime.now()
    # Concatena como strings (sem zero à esquerda)
    day = str(today.day)
    month = str(today.month)
    concatenated = int(day + month)  # Ex: 18 + 4 = "184"
    
    password_number = concatenated + pdv_number
    password = f"pdv@{password_number}"
    return password

def password_view(request):
    pdv_number = request.GET.get('pdv_number')
    password = None

    if pdv_number:
        try:
            pdv_number = int(pdv_number)

            # Dia e mês como strings SEM zero à esquerda
            today = datetime.now()
            day = str(today.day)
            month = str(today.month)

            # Cache key inclui pdv e concatenação (exata)
            cache_key = f"pdv_password_{pdv_number}_{day}{month}"

            password = cache.get(cache_key)

            if not password:
                password = calculate_password(pdv_number)
                cache.set(cache_key, password, 86400)  # Cache por 24h

        except ValueError:
            password = "Número de PDV inválido. Por favor, forneça um número válido."
    else:
        password = "Por favor, forneça o número do PDV."

    return render(request, 'pdv_password.html', {
        'password': password,
        'pdv_number': pdv_number
    })
