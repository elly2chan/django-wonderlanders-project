from django.contrib import admin

from wonderlanders.products.models import ProductCategory, Product


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    exclude = ('user', )
    list_display = ('title', )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('user', )
    list_display = ('name', 'price', 'category', 'destination', )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()
