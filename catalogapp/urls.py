from django.urls import path
from Django.catalogapp.apps import CatalogappConfig
from Django.catalogapp.views import home, contact

app_name = CatalogappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contact, name='contact')
]
