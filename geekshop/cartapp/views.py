from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from cartapp.models import Cart
from mainapp.models import Product


def cart(request):
    content = {}
    return render(request, 'cartapp/cart.html', content)


def cart_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    cart = Cart.objects.filter(user=request.user, product=product).first()
    if not cart:
        cart = Cart(user=request.user, product=product)

    cart.quantity += 1
    cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, pk):
    content = {}
    return render(request, 'cartapp/cart.html', content)