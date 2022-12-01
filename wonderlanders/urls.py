from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wonderlanders.common.urls')),
    path('posts/', include('wonderlanders.posts.urls')),
    path('profile/', include('wonderlanders.profiles.urls')),
    path('products/', include('wonderlanders.products.urls')),
    path('store/', include('wonderlanders.store.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
