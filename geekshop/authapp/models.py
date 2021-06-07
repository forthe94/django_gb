from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from cartapp.models import Cart
from mainapp.models import Product


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', blank=True, default=0)

    def get_cart_total(self):
        cart = Cart.objects.filter(user=self)
        ret_total = 0
        ret_count = 0
        for item in cart:
            cur_prod = Product.objects.filter(id=item.product_id).values()
            ret_total += cur_prod[0]['price'] * item.quantity
            ret_count += item.quantity
        return ret_total, ret_count
