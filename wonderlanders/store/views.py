from django.contrib.auth.decorators import login_required
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
    product = Product.objects.get(pk=pk)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url='index', redirect_field_name=None)
def item_clear(request, pk):
    cart = Cart(request)
    product = Product.objects.get(pk=pk)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url='index', redirect_field_name=None)
def item_increment(request, pk):
    cart = Cart(request)
    product = Product.objects.get(pk=pk)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url='index', redirect_field_name=None)
def item_decrement(request, pk):
    cart = Cart(request)
    product = Product.objects.get(pk=pk)
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

    products = Product.objects.all()

    context = {
        'cart_info': cart_info,
        'cart_total_price': cart_total_price,
        'total_price_with_vat': total_price_with_vat,
        'products': products,
    }
    return render(request, 'store/cart.html', context)


@method_decorator(login_required(login_url='index', redirect_field_name=None), name='dispatch')
class CheckoutView(views.CreateView):
    template_name = 'store/checkout.html'
    form_class = CheckoutForm

    def form_valid(self, form):
        checkout = form.save(commit=False)
        checkout.user = self.request.user
        checkout.order_total_price = cart_details(self.request)['cart_total_price_with_vat']
        checkout.order_products_quantity = cart_details(self.request)['cart_products_count']
        cart_clear(self.request)
        checkout.save()
        return render(self.request, 'store/successful_checkout.html')

    def get_initial(self):
        user = self.request.user
        return {'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}
