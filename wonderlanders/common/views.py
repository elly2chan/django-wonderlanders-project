from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.views import generic as views
from django.http import Http404

from wonderlanders.common.forms import ContactForm
from wonderlanders.common.models import Contact
from wonderlanders.posts.models import PostCategory, Post


class IndexView(views.TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            posts = Post.objects.all().order_by('id').reverse()
        except ObjectDoesNotExist:
            raise Http404

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

    def get_initial(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            return {'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}

    def form_valid(self, form):
        self.request.session['submit_redirect'] = True
        form.save()
        return redirect('contact submitted')


class ContactSubmittedView(views.TemplateView):
    template_name = 'common/contact_submitted.html'

    def get(self, request, *args, **kwargs):
        if 'submit_redirect' in self.request.session:
            context = self.get_context_data(**kwargs)
            del self.request.session['submit_redirect']
            return self.render_to_response(context)
        else:
            return redirect('index')
