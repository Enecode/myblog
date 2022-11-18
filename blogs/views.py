from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    return render(request, 'blogs/index.html')


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blogs/post_list.html', {'posts': posts})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'blogs/post_detail.html', {'post': post})


def contact(request):
    return render(request, 'blogs/contact.html')


def projects(request):
    return render(request, 'blogs/project.html')
