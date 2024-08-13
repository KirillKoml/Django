from django.shortcuts import render, get_object_or_404

from catalogapp.models import Product


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)


def contact(request):
    return render(request, "contacts.html")


def product(request):
    return render(request, "product.html")


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)
