from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog


# class BasePageView(TemplateView):
#     template_name = 'base.html'
#     model = Blog


class HomePageView(ListView):
    template_name = 'home.html'
    model = Blog


class PostDetailPageView(DetailView):
    model = Blog
    template_name = 'post_detail.html'


# class ModelDetailView(DetailView):
#     model = Blog
#     template_name = "post_detail.html"
