from django.urls import path, include
from catalogapp.apps import CatalogappConfig
from catalogapp.views import home

catalog_app = CatalogappConfig.name

urlpatterns = [
    path('', home, name='home')
]