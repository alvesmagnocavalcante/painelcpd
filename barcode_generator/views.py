from django.shortcuts import render
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.http import HttpResponse

def generate_barcode(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        if number:
            try:
                # Obtendo a classe do barcode
                code128 = barcode.get_barcode_class('code128')
                
                # Configurações ajustadas do ImageWriter
                # Usando a classe Code128 diretamente
                writer = ImageWriter()
                writer.dpi = 300
                writer.module_width = 0.2
                writer.module_height = 10
                writer.quiet_zone = 2
                
                code = Code128(number, writer=writer)
                
                # Gerando o código de barras e salvando na memória
                buffer = BytesIO()
                code.write(buffer)
                buffer.seek(0)
                
                # Preparando a resposta HTTP com o código de barras
                response = HttpResponse(buffer.getvalue(), content_type='image/png')
                response['Content-Disposition'] = 'inline; filename="barcode.png"'
                return response
            except Exception as e:
                return HttpResponse(f"Erro ao gerar o código de barras: {e}")
    return render(request, 'barcode_generator.html')
