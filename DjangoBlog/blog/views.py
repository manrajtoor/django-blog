from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
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