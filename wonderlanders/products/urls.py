from django.urls import path, include

from wonderlanders.products.views import ProductsView, AddProductView, AddProductCategoryView, EditProductView, \
    DeleteProductView, ProductCategories, EditProductCategoryView, DeleteProductCategoryView

urlpatterns = (
    path('', ProductsView.as_view(), name='all products'),
    path('add-product/', AddProductView.as_view(), name='add product'),
    path('add-product-category/', AddProductCategoryView.as_view(), name='add product category'),
    path('edit-product/<int:pk>', EditProductView.as_view(), name='edit product'),
    path('delete-product/<int:pk>', DeleteProductView.as_view(), name='delete product'),
    path('product-categories/', include([
        path('', ProductCategories.as_view(), name='product categories'),
        path('edit/<int:pk>', EditProductCategoryView.as_view(), name='edit product category'),
        path('delete/<int:pk>', DeleteProductCategoryView.as_view(), name='delete product category'),
    ])),
)
