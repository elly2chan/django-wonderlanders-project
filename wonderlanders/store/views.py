from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import generic as views
from cart.cart import Cart

from wonderlanders.common.context_processors import cart_details
from wonderlanders.products.models import Product
from wonderlanders.store.forms import CheckoutForm


@login_required(login_url='index', redirect_field_name=None)
def cart_add(request, pk):
    cart = Cart(request)

    try:
        product = Product.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404

    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url='index', redirect_field_name=None)
def item_clear(request, pk):
    cart = Cart(request)

    try:
        product = Product.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404

    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url='index', redirect_field_name=None)
def item_increment(request, pk):
    cart = Cart(request)

    try:
        product = Product.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404

    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url='index', redirect_field_name=None)
def item_decrement(request, pk):
    cart = Cart(request)

    try:
        product = Product.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404

    for key, value in cart.cart.items():
        if key == str(product.id):
            if value['quantity'] > 1:
                value['quantity'] = value['quantity'] - 1
            else:
                cart.remove(product)
            cart.save()

            return redirect('cart_detail')


@login_required(login_url='index', redirect_field_name=None)
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def get_cart_info(request):
    cart = Cart(request)
    cart_info = cart.cart.items()
    return cart_info


@login_required(login_url='index', redirect_field_name=None)
def cart_detail(request):
    cart_info = get_cart_info(request)
    cart_total_price = 0

    for key, value in cart_info:
        cart_total_price += value['quantity'] * float(value['price'])

    total_price_with_vat = cart_total_price * 1.2

    try:
        products = Product.objects.all()
    except ObjectDoesNotExist:
        raise Http404

    context = {
        'cart_info': cart_info,
        'cart_total_price': cart_total_price,
        'total_price_with_vat': total_price_with_vat,
        'products': products,
    }

    return render(request, 'store/cart.html', context)


@method_decorator(login_required(login_url='index', redirect_field_name=None), name='dispatch')
class CheckoutView(views.FormView):
    template_name = 'store/checkout.html'
    form_class = CheckoutForm

    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff or cart_details(self.request)['cart_products_count'] == 0:
            raise Http404
        context = self.get_context_data()
        return self.render_to_response(context)

    def form_valid(self, form):
        self.request.session['checkout_success_redirect'] = True
        checkout = form.save(commit=False)
        checkout.user = self.request.user
        checkout.order_total_price = cart_details(self.request)['cart_total_price_with_vat']
        checkout.order_products_quantity = cart_details(self.request)['cart_products_count']
        cart_clear(self.request)
        checkout.save()
        return redirect('checkout success')

    def get_initial(self):
        user = self.request.user
        return {'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}


class CheckoutSuccessView(views.TemplateView):
    template_name = 'store/successful_checkout.html'

    def get(self, request, *args, **kwargs):
        if 'checkout_success_redirect' in self.request.session:
            context = self.get_context_data(**kwargs)
            del self.request.session['checkout_success_redirect']
            return self.render_to_response(context)
        else:
            return redirect('index')
