from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Post, Image


class CategoryList(ListView):
    model = Category
    template_name = 'blog/Category_list.html'


def postList(request, slug):
    category = Category.objects.get(slug_url=slug)
    post_list = Post.objects.filter(category=category).order_by('-create_date')

    return render(
        request,
        'blog/Post_list.html',
        {
            'post_list': post_list,
            'category': category,
        }
    )


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/Post_detail.html'
