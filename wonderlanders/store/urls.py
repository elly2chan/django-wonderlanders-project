from django.urls import path

from wonderlanders.store.views import cart_add, item_clear, item_increment, item_decrement, cart_clear, cart_detail, \
    CheckoutView

urlpatterns = (
    path('cart/add/<int:pk>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:pk>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:pk>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:pk>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail, name='cart_detail'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
)
