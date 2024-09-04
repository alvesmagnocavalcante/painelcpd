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
                # Obtendo a classe Code128 do barcode
                code128_class = barcode.get_barcode_class('code128')
                
                # Configurações ajustadas do ImageWriter
                writer = ImageWriter()
                writer.dpi = 300  # Resolução de imagem
                writer.module_width = 0.2  # Largura ajustada dos módulos para reduzir o tamanho
                writer.module_height = 8  # Altura ajustada dos módulos para reduzir o tamanho
                writer.quiet_zone = 1  # Área silenciosa ajustada para reduzir o tamanho
                
                # Gerando o código de barras
                code = code128_class(number, writer=writer)
                
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
    return render(request, 'barcode_generator.html')
