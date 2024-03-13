# Create your views here.
from django.http import JsonResponse
from e_commerce.models import Comic


def comic_list_api_view(request):
    if request.method == 'GET':
        # Alumno:
        # Deberá completar el funcionamiento de este endpoint.
        # Seguir los pasos detallados en
        # el archivo de enunciado de tarea
        print("Endpoint: comic_list_api_view")
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)