from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from wonderlanders.core.view_mixins import PostAuthorRequiredMixin
from wonderlanders.posts.forms import CreatePostForm, EditPostForm, CommentForm
from wonderlanders.posts.models import PostCategory, Post, PostComment


@method_decorator(login_required(login_url='index', redirect_field_name=None), name='dispatch')
class CreatePostView(views.FormView):
    model = Post
    form_class = CreatePostForm
    template_name = 'posts/create_post.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return redirect('index')


@method_decorator(login_required(login_url='index', redirect_field_name=None), name='dispatch')
class PostDetailsView(views.DetailView):
    model = Post
    template_name = 'posts/post_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['category'] = PostCategory.objects.filter(id=self.object.category_id)
            context['category_posts'] = Post.objects.filter(category=self.object.category).exclude(id=self.object.id)
            context['post_comments'] = PostComment.objects.filter(post_id=self.object.id)
        except ObjectDoesNotExist:
            raise Http404

        context['last_comment'] = context['post_comments'].last()
        context['form'] = CommentForm()
        return context


class PostCategoryView(views.DetailView):
    model = PostCategory
    template_name = 'posts/post_category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            posts = Post.objects.filter(category_id=self.object.id).order_by('id').reverse()
        except ObjectDoesNotExist:
            raise Http404

        page = self.request.GET.get('page')
        context['posts'] = Paginator(posts, 30).get_page(page)

        try:
            context['categories'] = PostCategory.objects.all()
        except ObjectDoesNotExist:
            raise Http404

        return context


@method_decorator(login_required(login_url='index', redirect_field_name=None), name='dispatch')
class EditPostView(PostAuthorRequiredMixin, views.UpdateView):
    template_name = 'posts/edit_post.html'
    model = Post
    form_class = EditPostForm

    def get_success_url(self):
        return reverse_lazy('post details', kwargs={
            'pk': self.object.pk,
        })


@method_decorator(login_required(login_url='index', redirect_field_name=None), name='dispatch')
class DeletePostView(PostAuthorRequiredMixin, views.DeleteView):
    template_name = 'posts/delete_post.html'
    model = Post
    success_url = reverse_lazy('index')


@login_required
def comment_post(request, pk):

    try:
        post = Post.objects.filter(pk=pk) \
            .get()
    except ObjectDoesNotExist:
        raise Http404

    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()

    return redirect('post details', pk)


@login_required
def delete_comment(request, pk):

    try:
        comment = PostComment.objects.filter(pk=pk).get()
    except ObjectDoesNotExist:
        raise Http404

    if comment.user == request.user or request.user.is_superuser:
        comment.delete()
    return redirect('post details', comment.post.pk)
