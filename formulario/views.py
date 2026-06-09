from django.shortcuts import render
from .models import Contato

def formulario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')

        Contato.objects.create(
            nome=nome,
            email=email
        )

    return render(request, 'formulario.html')