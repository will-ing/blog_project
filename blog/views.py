from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog


class HomePageView(ListView):
    template_name = 'home.html'
    model = Blog


class PostDetailPageView(DetailView):
    model = Blog
    template_name = 'post_detail.html'
