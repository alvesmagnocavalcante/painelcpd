from django.shortcuts import render
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader  # Importação corrigida

def generate_barcode(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        if number and len(number) == 6:  # Verifica se o número possui 6 dígitos
            try:
                # Preenchendo com zeros à esquerda para totalizar 12 dígitos
                full_number = number.zfill(12)
                
                # Configurações do gerador de código de barras
                ean13_class = barcode.get_barcode_class('ean13')
                writer = ImageWriter()
                writer.dpi = 250
                writer.module_width = 0.3
                writer.module_height = 15
                writer.quiet_zone = 6
                writer.font_size = 0
                
                # Gerar os códigos de barras e salvar em uma lista de imagens
                images = []
                for _ in range(5):
                    buffer = BytesIO()
                    code = ean13_class(full_number, writer=writer)
                    code.write(buffer, text='')
                    buffer.seek(0)
                    images.append(ImageReader(buffer))  # Converte para ImageReader diretamente

                # Gerar o PDF com os códigos de barras
                pdf_buffer = BytesIO()
                pdf_canvas = canvas.Canvas(pdf_buffer, pagesize=A4)
                width, height = A4
                x, y = 50, height - 100  # Posição inicial do primeiro código
                
                for img in images:
                    # Inserir a imagem no PDF
                    pdf_canvas.drawImage(img, x, y, width=200, height=50)
                    y -= 70  # Atualizar a posição para o próximo código
                    if y < 50:  # Nova página, se necessário
                        pdf_canvas.showPage()
                        y = height - 100
                
                pdf_canvas.save()
                pdf_buffer.seek(0)
                
                # Retornar o PDF como resposta HTTP para exibição
                response = HttpResponse(pdf_buffer, content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="barcodes.pdf"'
                return response

            except Exception as e:
                return HttpResponse(f"Erro ao gerar o código de barras: {e}")
        else:
            return HttpResponse("O código deve ter exatamente 6 dígitos.")
    return render(request, 'barcode_generator.html')
