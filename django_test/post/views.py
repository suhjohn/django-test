from django.shortcuts import render

# Create your views here.
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context= {
        'posts':posts,
    }
    return render(request, 'post_list.html', context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post':post,
    }
    return render(request, 'post_detail.html', context)