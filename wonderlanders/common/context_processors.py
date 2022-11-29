from cart.cart import Cart


def cart_details(request):
    cart = Cart(request)
    cart_info = cart.cart.items()
    cart_products_count = 0
    cart_total_price = 0

    for key, value in cart_info:
        cart_products_count += value['quantity']
        cart_total_price += value['quantity'] * float(value['price'])
    cart_total_price_with_vat = cart_total_price * 1.2

    return {
        'cart_products_count': cart_products_count,
        'cart_total_price': cart_total_price,
        'cart_total_price_with_vat': cart_total_price_with_vat,
    }
