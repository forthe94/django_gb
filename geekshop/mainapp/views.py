from django.shortcuts import render
from .models import ProductCategory, Product
from cartapp.models import Cart
# Create your views here.
from django.shortcuts import get_object_or_404
from django.shortcuts import render
import random


def get_cart(user):
    if user.is_authenticated:
        return Cart.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category). \
                        exclude(pk=hot_product.pk)[:3]

    return same_products

def main(request):
    socials = ['socail' + str(i) for i in range(4)]
    products = Product.objects.all()[:4]

    content = {
        'products': products,
        'socials': socials
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None):
    socials = ['social' + str(i) for i in range(4)]

    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    total = 0
    total_items = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        total, total_items = request.user.get_cart_total()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'socials': socials,
            'total': total,
            'total_items': total_items
        }
        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'hot_product': hot_product,
        'socials': socials,
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    socials = ['social' + str(i) for i in range(4)]
    content = {
        'socials': socials
    }
    return render(request, 'mainapp/contact.html', context=content)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'cart': get_cart(request.user),
    }

    return render(request, 'mainapp/product.html', content)