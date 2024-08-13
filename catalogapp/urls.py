from django.urls import path
from catalogapp.apps import CatalogappConfig
from catalogapp.views import home, contact, product_detail, product

app_name = CatalogappConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contact, name="contact"),
    path("product/", product, name="product"),
    path('product/<int:pk>/', product_detail, name='product_detail'),
]
