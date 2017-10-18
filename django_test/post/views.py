from django.shortcuts import render, redirect

# Create your views here.
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)


def post_create(request):
    """
    POST 일 경우 Post object 만든 후 post_list로 redirect

    :param request:
    :return:
    """
    if request.method == 'POST' and request.POST['title']:
        post = Post.objects.create(title=request.POST['title'])
        print(post)
        if post:
            return redirect(post_list)

    return render(request, 'post_create.html')


def post_delete(request):
    if request.method == 'POST':
        pass

    else:
        return redirect(post_list)
