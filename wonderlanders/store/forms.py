from django import forms

from wonderlanders.core.form_mixins import AddPlaceholdersFormMixin, RemoveLabelsFormMixin, AddStyleClassFormMixin
from wonderlanders.store.models import Order

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CheckoutForm(AddPlaceholdersFormMixin, RemoveLabelsFormMixin, AddStyleClassFormMixin, forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user', 'order_date', )
        labels = {
            'country': 'CHOOSE YOUR COUNTRY:',
        }

        widgets = {
            'order_total_price': forms.HiddenInput(),
            'order_products_quantity': forms.HiddenInput(),
        }
