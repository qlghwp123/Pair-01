from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):

    data = Post.objects.all().order_by('id')

    return render(request, 'movies/index.html', {'data': data})

def detail(request):
    pass

def write(request):

    _title = request.GET.get('title')
    _content = request.GET.get('content')

    Post.objects.create(title=_title, content=_content)

    return redirect('movies:index')

def modify(request):
    pass

def delete(request):
    pass
