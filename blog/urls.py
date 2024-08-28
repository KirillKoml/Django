from django.urls import path
from blog.apps import BlogsConfig
from blog.views import BlogsListView, BlogsDetailView, BlogsCreateView, BlogsUpdateView, BlogsDeleteView

app_name = BlogsConfig.name


urlpatterns = [
    path('list/', BlogsListView.as_view(), name='blog_list'),
    path('view/<int:pk>/', BlogsDetailView.as_view(), name='view'),
    path('create/', BlogsCreateView.as_view(), name='blog_create'),
    path('edit/<int:pk>/', BlogsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogsDeleteView.as_view(), name='delete'),
]
