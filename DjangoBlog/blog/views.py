from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy


class IndexView(ListView):
    model = Post
    template_name = "index.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_details.html"

class CreatePostView(CreateView):
    model = Post
    template_name = "create_post.html"
    fields = ('title', 'author', 'body')

class UpdatePostView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ['title', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('index')

class AddCommentView(CreateView):
    model = Comment
    template_name = "add_comment.html"
    fields = ('name', 'body')
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)