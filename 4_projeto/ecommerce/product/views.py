from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from . import models


class ListProduct(ListView):
    model = models.Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 3


class DetailProduct(DetailView):
    model = models.Product
    template_name = 'product/detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


class AddCart(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('product:list')
        )
        variation_id = self.request.GET.get('vid')

        if not variation_id:
            messages.error(
                self.request,
                'Produto não existe'
            )
            return redirect(http_referer)

        variation = get_object_or_404(models.Variation, id=variation_id)
        variation_stock = variation.stock
        product = variation.product

        product_id = product.id
        product_name = product.name
        variation_name = variation.name or ''
        price = variation.price
        price_promotional = variation.price_promotional
        quantity = 1
        slug = product.slug
        image = product.image

        if image:
            image = image.name
        else:
            image = ''

        if variation.stock < 1:
            messages.error(
                self.request,
                'Estoque insuficiente'
            )
            return redirect(http_referer)

        if not self.request.session.get('cart'):
            self.request.session['cart'] = {}
            self.request.session.save()

        cart = self.request.session['cart']

        if variation_id in cart:
            quantity_cart = cart[variation_id]['quantity']
            quantity_cart += 1

            if variation_stock < quantity_cart:
                messages.warning(
                    self.request,
                    f'Estoque insuficiente'
                )
                quantity_cart = variation_stock

            cart[variation_id]['quantity'] = quantity_cart
            cart[variation_id]['price_quantity'] = price * quantity_cart
            cart[variation_id]['price_quantity_promotional'] = price_promotional * quantity_cart
        else:
            cart[variation_id] = {
                'product_id': product_id,
                'product_name': product_name,
                'variation_id': variation_id,
                'variation_name': variation_name,
                'price': price,
                'price_promotional': price_promotional,
                'price_quantity': price,
                'price_quantity_promotional': price_promotional,
                'quantity': 1,
                'slug': slug,
                'image': image,
            }

        self.request.session.save()

        messages.success(
            self.request,
            f'"{product_name} {variation_name}" adicionado no seu carrinho!'
        )

        return redirect(http_referer)


class RemoveCart(View):
    pass


class Cart(View):
    pass


class Finalizar(View):
    pass
