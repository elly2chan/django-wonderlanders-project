from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic as views

from wonderlanders.common.forms import ContactForm
from wonderlanders.common.models import Contact
from wonderlanders.posts.models import PostCategory, Post


class IndexView(views.TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all().order_by('id').reverse()
        page = self.request.GET.get('page')
        context['posts'] = Paginator(posts, 30).get_page(page)
        context['categories'] = PostCategory.objects.all()
        return context


class AboutView(views.TemplateView):
    template_name = 'common/about.html'


class ContactView(views.FormView):
    model = Contact
    form_class = ContactForm
    template_name = 'common/contact.html'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'common/contact_submitted.html')

    def get_initial(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            return {'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}


def error_404_view(request):
    return render(request, 'common/page_not_found_404.html')
