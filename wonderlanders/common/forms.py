from django import forms

from wonderlanders.common.models import Contact
from wonderlanders.core.form_mixins import RemoveLabelsFormMixin, AddPlaceholdersFormMixin, AddStyleClassFormMixin


class ContactForm(AddPlaceholdersFormMixin, RemoveLabelsFormMixin, AddStyleClassFormMixin, forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('answered', )

        widgets = {
            'message': forms.Textarea(),
        }
