from django.urls import path, include

from wonderlanders.posts.views import PostDetailsView, \
    CreatePostView, PostCategoryView, EditPostView, DeletePostView, comment_post, delete_comment

urlpatterns = (
    path('create/', CreatePostView.as_view(), name='create post'),
    path('details/<int:pk>', PostDetailsView.as_view(), name='post details'),
    path('category/<slug>', PostCategoryView.as_view(), name='post category'),
    path('edit/<int:pk>', EditPostView.as_view(), name='edit post'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete post'),
    path('comment/<int:pk>/', include([
        path('', comment_post, name='comment post'),
        path('delete/', delete_comment, name='delete comment'),
    ])),
)
