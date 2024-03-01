# Create your views here.
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from e_commerce.models import Comic


def comic_retrieve_api_view(request):
    if request.method == 'GET':
        instance = Comic.objects.filter(id=request.GET.get('id')).first()
        if instance:
            return JsonResponse(data=model_to_dict(instance), status=200)
        return JsonResponse(data={}, status=404)
    else:
        return JsonResponse(
            data={"message": "Método HTTP no permitido."},
            status=405
        )


def comic_list_api_view(request):
    if request.method == 'GET':
        _queryset = Comic.objects.all()
        _data = list(_queryset.values()) if _queryset.exists() else []
        return JsonResponse(data=_data, safe=False, status=200)
    else:
        return JsonResponse(
            data={"message": "Método HTTP no permitido."},
            status=405
        )

@csrf_exempt
def comic_create_api_view(request):
    if request.method == 'POST':
        # Casteo el query-dict request.POST a un dict para poder aplicar
        # método .pop() ya que el query-dict es inmutable.
        _request = dict(request.POST)
        _marvel_id = _request.pop('marvel_id', None)
        if not _marvel_id:
            return JsonResponse(
                data={"marvel_id": "Este campo no puede ser nulo."},
                status=400
            )
        _instance, _created = Comic.objects.get_or_create(
            marvel_id=_marvel_id,
            defaults=_request.POST
        )
        if _created:
            return JsonResponse(
                data=model_to_dict(_instance), status=201
            )
        return JsonResponse(
            data={
                "marvel_id": "Ya existe un comic con ese valor, debe ser único."
            },
            status=400
        )
    else:
        return JsonResponse(
            data={"message": "Método HTTP no permitido."},
            status=405
        )
