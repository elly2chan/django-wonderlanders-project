from django.urls import path

from wonderlanders.common.views import IndexView, AboutView, ContactView, ContactSubmittedView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact-submitted/', ContactSubmittedView.as_view(), name='contact submitted'),
)
