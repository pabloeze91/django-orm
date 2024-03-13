import pytest
from pytest_fixtures import *

from django.urls import reverse
from django.core.management import call_command

from rest_framework import status

from e_commerce import models


@pytest.mark.django_db
def test_comic_list(client):

    call_command('get_comics')

    endpoint_url = reverse('comic_list_api_view')
    response = client.get(endpoint_url)

    assert response.status_code == status.HTTP_200_OK, 'El endpoint falló al ejecutarse'

    data = response.json()
    print(f"Tipo de dato retornado por la vista: {type(data)}")
    assert isinstance(data, list), f'Se espera que el endpoint retorne una lista'

    print(f"Cuantos comics retornó el enpdoint en la lista: {len(data)}")
    assert len(data), 'La lista de comics no debe estar vacía'