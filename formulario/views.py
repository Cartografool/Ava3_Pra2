import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Contato

@csrf_exempt
def receber_formulario(request):
    if request.method == "POST":
        dados = json.loads(request.body)

        nome = dados.get("nome")
        email = dados.get("email")

        Contato.objects.create(
            nome=nome,
            email=email
        )

        return JsonResponse({
            "sucesso": True,
            "nome": nome,
            "email": email
        })

    return JsonResponse({"erro": "Método inválido"})