from django.urls import path
from e_commerce.views import *


urlpatterns = [
    path('comic-list/', comic_list_api_view, name="comic_list_api_view"),
]
