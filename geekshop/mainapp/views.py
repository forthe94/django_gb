from django.shortcuts import render
from .models import ProductCategory, Product
# Create your views here.

from django.shortcuts import render


def main(request):
    socials = ['socail' + str(i) for i in range(4)]
    products = Product.objects.all()[:4]

    content = {
        'products': products,
        'socials': socials
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    products_links = ['все', 'дом', 'офис', 'модерн', 'классика']
    socials = ['social' + str(i) for i in range(4)]
    print(socials)
    content = {
        'products_links': products_links,
        'socials': socials
    }
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    socials = ['social' + str(i) for i in range(4)]
    print(socials)
    content = {
        'socials': socials
    }
    return render(request, 'mainapp/contact.html', context=content)