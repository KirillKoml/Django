from django.urls import path, include
from catalogapp.apps import CatalogappConfig
from catalogapp.views import home

app_name = CatalogappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contact, name='contact')
]
