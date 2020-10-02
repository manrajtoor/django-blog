from django.urls import path
from .views import IndexView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView, AddCommentView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post"),
    path('create_post/', CreatePostView.as_view(), name="create_post" ),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name="delete_post"),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment")
]
