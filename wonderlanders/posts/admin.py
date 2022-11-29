from django.contrib import admin

from wonderlanders.posts.models import PostCategory, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('title', 'destination', 'description')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    exclude = ('user', )
    list_display = ('id', 'title',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()
