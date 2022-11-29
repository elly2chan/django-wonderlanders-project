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


class SearchPostsForm(forms.Form):
    MAX_SEARCH_LENGTH = 30
    post_title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search...',
            'style': 'max-width: 300px',
        }),
        max_length=MAX_SEARCH_LENGTH,
        required=False,
        label="",
    )
