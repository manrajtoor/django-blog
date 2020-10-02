from django.urls import path
from .views import IndexView, PostDetailView, CreatePostView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post"),
    path('create_post/', CreatePostView.as_view(), name="create_post" )
]
