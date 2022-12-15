from django import forms

from wonderlanders.core.form_mixins import AddPlaceholdersFormMixin, RemoveLabelsFormMixin, AddStyleClassFormMixin
from wonderlanders.store.models import Order


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
