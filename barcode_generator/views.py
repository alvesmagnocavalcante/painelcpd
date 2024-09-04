from django.shortcuts import render
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.http import HttpResponse

def generate_barcode(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        
        if number and len(number) == 12:
            try:
                # Obtendo a classe EAN13 do barcode
                ean_class = barcode.get_barcode_class('ean13')
                
                # Configurações ajustadas do ImageWriter
                writer = ImageWriter()
                writer.dpi = 300  # Resolução de imagem
                writer.module_width = 0.2  # Largura ajustada dos módulos
                writer.module_height = 15  # Altura ajustada dos módulos
                writer.quiet_zone = 2  # Área silenciosa ajustada
                
                # Gerando o código de barras
                code = ean_class(number, writer=writer)
                
                # Salvando o código de barras na memória
                buffer = BytesIO()
                code.write(buffer, options={"write_text": False})  # Desativar o texto por padrão
                buffer.seek(0)
                
                # Preparando a resposta HTTP com o código de barras
                response = HttpResponse(buffer.getvalue(), content_type='image/png')
                response['Content-Disposition'] = 'inline; filename="barcode.png"'
                return response
            except Exception as e:
                return HttpResponse(f"Erro ao gerar o código de barras: {e}")
        else:
            return HttpResponse("Número inválido! Certifique-se de que ele possui 12 dígitos.")
    return render(request, 'barcode_generator.html')
