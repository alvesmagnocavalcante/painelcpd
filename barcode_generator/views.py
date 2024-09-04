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
                writer.dpi = 150  # Resolução de imagem maior para maior clareza
                writer.module_width = 0.3  # Largura dos módulos aumentada para melhorar a leitura
                writer.module_height = 15  # Altura dos módulos aumentada para maior visibilidade
                writer.quiet_zone = 6  # Área silenciosa aumentada para melhor leitura
                writer.font_size = 0  # Tamanho da fonte desativado para não mostrar texto
                
                # Gerando o código de barras
                code = code128_class(number, writer=writer)
                
                # Salvando o código de barras na memória
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
