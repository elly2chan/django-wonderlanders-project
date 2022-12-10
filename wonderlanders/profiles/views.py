from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth import authenticate, login

from wonderlanders.core.view_mixins import AccountOwnerRequiredMixin
from wonderlanders.profiles.decorators import restrict_access_to_logged_in_users
from wonderlanders.profiles.forms import UserCreateForm, UserEditForm, LoginForm
from wonderlanders.posts.models import Post


UserModel = get_user_model()


@method_decorator(restrict_access_to_logged_in_users(), name='dispatch')
class LoginView(auth_views.LoginView):
    template_name = 'profiles/login.html'
    form_class = LoginForm


@method_decorator(restrict_access_to_logged_in_users(), name='dispatch')
class RegisterView(views.CreateView):
    template_name = 'profiles/register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect(self.success_url)


@method_decorator(login_required(login_url='index', redirect_field_name=None), name='dispatch')
class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(AccountOwnerRequiredMixin, views.DetailView):
    template_name = 'profiles/profile_details.html'
    model = UserModel
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            posts = Post.objects.filter(user_id=self.request.user.id).order_by('id')
        except ObjectDoesNotExist:
            raise Http404

        page = self.request.GET.get('page')
        context['posts'] = Paginator(posts, 30).get_page(page)
        context['posts_count'] = posts.count()
        return context


class UserEditView(AccountOwnerRequiredMixin, views.UpdateView):
    template_name = 'profiles/edit_profile.html'
    model = UserModel
    context_object_name = 'profile'
    form_class = UserEditForm

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(AccountOwnerRequiredMixin, views.DeleteView):
    template_name = 'profiles/delete_profile.html'
    model = UserModel
    success_url = reverse_lazy('index')
