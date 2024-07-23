from django.urls import path
from catalogapp.apps import CatalogappConfig
from catalogapp.views import home, contact

app_name = CatalogappConfig.name

urlpatterns = [path("", home, name="home"), path("contacts/", contact, name="contact")]
