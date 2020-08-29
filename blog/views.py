from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blog


class HomePageView(ListView):
    template_name = 'home.html'
    model = Blog


class PostDetailPageView(DetailView):
    model = Blog
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'create.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'edit.html'
    fields = ['title', 'author', 'body']


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
