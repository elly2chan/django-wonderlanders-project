from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from wonderlanders.core.form_mixins import AddPlaceholdersFormMixin, AddStyleClassFormMixin, RemoveLabelsFormMixin

UserModel = get_user_model()


class UserEditForm(AddPlaceholdersFormMixin, AddStyleClassFormMixin, forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'profile_picture')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'profile_picture': 'Profile Picture URL',
        }


class UserCreateForm(AddPlaceholdersFormMixin, RemoveLabelsFormMixin, AddStyleClassFormMixin, UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'PASSWORD',
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'CONFIRM PASSWORD',
        })
    )

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None

    class Meta:
        model = UserModel
        fields = ('username', 'email')


class LoginForm(AddPlaceholdersFormMixin, RemoveLabelsFormMixin, AddStyleClassFormMixin, AuthenticationForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'PASSWORD',
        }))
