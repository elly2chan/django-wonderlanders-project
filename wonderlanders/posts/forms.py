from django import forms

from wonderlanders.core.form_mixins import AddStyleClassFormMixin, RemoveLabelsFormMixin, AddPlaceholdersFormMixin
from wonderlanders.posts.models import Post, PostComment


class CreatePostForm(AddPlaceholdersFormMixin, RemoveLabelsFormMixin, AddStyleClassFormMixin, forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', )
        labels = {
            'category': 'CHOOSE A CONTINENT',
        }

        widgets = {
            'description': forms.Textarea(),
        }


class EditPostForm(AddPlaceholdersFormMixin, RemoveLabelsFormMixin, AddStyleClassFormMixin, forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'destination', 'description', 'category')

        widgets = {
            'description': forms.Textarea(),
        }


class CommentForm(RemoveLabelsFormMixin, forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('comment', )
        widgets = {
            'comment': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Add comment...',
                    'style': 'max-width: 500px',
                },
            ),
        }
