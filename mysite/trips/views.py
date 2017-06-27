from django.shortcuts import render
from datetime import datetime
from trips.models import Post
from trips.models import ContactInfo
from django.http import HttpResponse


def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
        'baba': 'afternoon'
    })


def home(request):
    # get all posts
    post_list = Post.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        post = None
    return render(request, 'post.html', {'post': post})


def show_form(request, name):
    person = ContactInfo.objects.filter(name=name)
    return render(request, 'testForm.html', {'name': 'name'})

