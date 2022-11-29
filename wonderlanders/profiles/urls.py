from django.urls import path, include

from wonderlanders.profiles.views import LoginView, RegisterView, LogoutView, \
    UserDetailsView, UserEditView, UserDeleteView

urlpatterns = (
    path('login/', LoginView.as_view(), name='login user'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('logout/', LogoutView.as_view(), name='logout user'),
    path('<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)
