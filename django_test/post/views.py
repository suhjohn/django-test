from django.shortcuts import render

# Create your views here.
from .models import Post


def post_list(request):
    post = Post.objects.all()
    context= {
        'post':post,
    }
    return render(request, 'post_list.html', context)