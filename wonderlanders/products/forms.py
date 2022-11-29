from django import forms

from wonderlanders.core.form_mixins import AddPlaceholdersFormMixin, RemoveLabelsFormMixin, AddStyleClassFormMixin
from wonderlanders.products.models import Product, ProductCategory


class AddProductForm(AddPlaceholdersFormMixin, RemoveLabelsFormMixin, AddStyleClassFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user', )
        labels = {
            'category': 'CHOOSE PRODUCT CATEGORY',
        }


class AddProductCategoryForm(AddPlaceholdersFormMixin, RemoveLabelsFormMixin, AddStyleClassFormMixin, forms.ModelForm):
    class Meta:
        model = ProductCategory
        exclude = ('slug', 'user', )


class EditProductForm(AddPlaceholdersFormMixin, RemoveLabelsFormMixin, AddStyleClassFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'category', 'destination' )
        labels = {
            'category': 'PRODUCT CATEGORY',
        }


class EditProductCategoryForm(AddPlaceholdersFormMixin, RemoveLabelsFormMixin, AddStyleClassFormMixin, forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('title', )

