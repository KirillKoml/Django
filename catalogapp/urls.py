from django.urls import path
from catalogapp.apps import CatalogappConfig
from catalogapp.views import ProductListView, ProductDetailView, ContactListView, ProductCreateView, productUpdateView, productDeleteView

app_name = CatalogappConfig.name




urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path("contacts/", ContactListView.as_view(), name="contact_list"),
    path('product/<int:pk>/update/', productUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', productDeleteView.as_view(), name='product_delete'),
]