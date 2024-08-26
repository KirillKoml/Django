from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalogapp.models import Product, Contact


class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class ContactListView(ListView):
    model = Contact

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'category']
    success_url = reverse_lazy('catalogapp:product_list')

class productUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'category']
    success_url = reverse_lazy('catalogapp:product_list')

    def get_success_url(self):
        return reverse('catalogapp:product_detail', args=[self.kwargs.get('pk')])

class productDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalogapp:product_list')