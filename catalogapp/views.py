from django.shortcuts import render

from catalogapp.models import Product


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "home.html", context)


def contact(request):
    return render(request, "contacts.html")


def product(request):
    return render(request, "product.html")
