from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from wonderlanders.products.forms import AddProductForm, AddProductCategoryForm, EditProductForm, \
    EditProductCategoryForm
from wonderlanders.products.models import Product, ProductCategory


class ProductsView(views.TemplateView):
    template_name = 'products/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['categories'] = ProductCategory.objects.all()
        return context


@method_decorator(staff_member_required(login_url='index', redirect_field_name=None), name='dispatch')
class AddProductView(views.CreateView):
    model = Product
    form_class = AddProductForm
    template_name = 'products/add_product.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super(AddProductView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('all products')


@method_decorator(staff_member_required(login_url='index', redirect_field_name=None), name='dispatch')
class AddProductCategoryView(views.CreateView):
    model = ProductCategory
    form_class = AddProductCategoryForm
    template_name = 'products/add_product_category.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super(AddProductCategoryView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('all products')


@method_decorator(staff_member_required(login_url='index', redirect_field_name=None), name='dispatch')
class EditProductView(views.UpdateView):
    template_name = 'products/edit_product.html'
    model = Product
    form_class = EditProductForm

    def get_success_url(self):
        return reverse_lazy('all products')


@method_decorator(staff_member_required(login_url='index', redirect_field_name=None), name='dispatch')
class DeleteProductView(views.DeleteView):
    template_name = 'products/delete_product.html'
    model = Product
    success_url = reverse_lazy('all products')


@method_decorator(staff_member_required(login_url='index', redirect_field_name=None), name='dispatch')
class ProductCategories(views.ListView):
    model = ProductCategory
    template_name = 'products/product_categories.html'


@method_decorator(staff_member_required(login_url='index', redirect_field_name=None), name='dispatch')
class EditProductCategoryView(views.UpdateView):
    template_name = 'products/edit_category.html'
    model = ProductCategory
    form_class = EditProductCategoryForm

    def get_success_url(self):
        return reverse_lazy('product categories')


@method_decorator(staff_member_required(login_url='index', redirect_field_name=None), name='dispatch')
class DeleteProductCategoryView(views.DeleteView):
    template_name = 'products/delete_category.html'
    model = ProductCategory
    success_url = reverse_lazy('product categories')
