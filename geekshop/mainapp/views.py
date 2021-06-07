from django.shortcuts import render
from .models import ProductCategory, Product
from cartapp.models import Cart
# Create your views here.
from django.shortcuts import get_object_or_404
from django.shortcuts import render


def main(request):
    socials = ['socail' + str(i) for i in range(4)]
    products = Product.objects.all()[:4]

    content = {
        'products': products,
        'socials': socials
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None):
    print(pk)
    socials = ['social' + str(i) for i in range(4)]

    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    cart = []
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)

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
            'cart':cart,
        }
        print(content)
        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'socials': socials
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    socials = ['social' + str(i) for i in range(4)]
    print(socials)
    content = {
        'socials': socials
    }
    return render(request, 'mainapp/contact.html', context=content)
