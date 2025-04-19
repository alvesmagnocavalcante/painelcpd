from django.shortcuts import render
from datetime import datetime

def calculate_password(pdv_number):
    today = datetime.now()

    # Concatenação como string SEM zero à esquerda
    day = str(today.day)    # exemplo: '18'
    month = str(today.month)  # exemplo: '4'

    # Concatenação correta: '18' + '4' = '184'
    day_month_concat = int(day + month)  # 184

    print(f"[DEBUG] Dia: {day}, Mês: {month}, Concatenado: {day + month}, Resultado: {day_month_concat}")

    password_number = day_month_concat + pdv_number
    password = f"pdv@{password_number}"
    print(f"[DEBUG] PDV: {pdv_number}, Senha: {password}")
    return password

def password_view(request):
    pdv_number = request.GET.get('pdv_number')
    password = None

    if pdv_number:
        try:
            pdv_number = int(pdv_number)

            # Sem cache por enquanto
            password = calculate_password(pdv_number)

        except ValueError:
            password = "Número de PDV inválido. Por favor, forneça um número válido."
    else:
        password = "Por favor, forneça o número do PDV."

    return render(request, 'pdv_password.html', {
        'password': password,
        'pdv_number': pdv_number
    })
