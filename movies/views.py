from django.shortcuts import render, redirect
from .models import Post
import datetime


# Create your views here.
def index(request):
    data = Post.objects.all().order_by('id')

    return render(request, 'movies/index.html', {'data': data})


def detail(request, _id):
    data = Post.objects.get(id=_id)

    return render(request, 'movies/detail.html', {'data': data})


def write(request):
    _title = request.GET.get('title')
    _content = request.GET.get('content')

    Post.objects.create(title=_title, content=_content)

    return redirect('movies:index')


def update(request, _id):
    target = Post.objects.get(id=_id)
    target.title = request.GET.get('title')
    target.content = request.GET.get('content')
    target.updated_at = datetime.date.today()
    target.save()

    return redirect('movies:detail', _id)


def delete(request, _id):
    Post.objects.get(id=_id).delete()

    return redirect('movies:index')
