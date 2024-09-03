from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from openpyxl import Workbook
from .models import Balanca

def registro_balanca(request):
    if request.method == 'POST':
        numero_balanca = request.POST.get('numero_balanca')
        peso = request.POST.get('peso')
        setor = request.POST.get('setor')

        Balanca.objects.create(numero_balanca=numero_balanca, peso=peso, setor=setor)

        return redirect('lista_balanca')

    return render(request, 'registro_balanca.html')

def lista_balanca(request):
    registros = Balanca.objects.all()
    return render(request, 'lista_balanca.html', {'registros': registros})

def exportar_balanca_xlsx(request):
    registros = Balanca.objects.all()
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Registros de Balança"
    
    ws.append(['Número da Balança', 'Peso', 'Setor', 'Data de Registro', 'Status'])
    
    for registro in registros:
        if registro.peso < 19995:
            status = "Fora da margem"
        elif registro.peso == 19995:
            status = "Aceitável"
        else:
            status = "Dentro da margem"
        
        data_registro = registro.data_registro.replace(tzinfo=None) if registro.data_registro else None
        ws.append([registro.numero_balanca, registro.peso, registro.setor, data_registro, status])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=registros_balanca.xlsx'
    
    wb.save(response)
    return response

def editar_balanca(request, pk):
    balanca = get_object_or_404(Balanca, pk=pk)
    if request.method == 'POST':
        balanca.numero_balanca = request.POST.get('numero_balanca')
        balanca.peso = request.POST.get('peso')
        balanca.setor = request.POST.get('setor')
        balanca.save()

        return redirect('lista_balanca')

    return render(request, 'editar_balanca.html', {'balanca': balanca})

def excluir_balanca(request, pk):
    balanca = get_object_or_404(Balanca, pk=pk)
    if request.method == 'POST':
        balanca.delete()
        return redirect('lista_balanca')

    return render(request, 'excluir_balanca.html', {'balanca': balanca})
