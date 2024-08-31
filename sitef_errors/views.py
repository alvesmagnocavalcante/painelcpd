from django.shortcuts import render
from .models import SitefError

def search_error(request):
    query = request.GET.get('q')
    error = None
    if query:
        error = SitefError.objects.filter(code=query).first()
    return render(request, 'search_error.html', {'error': error, 'query': query})
