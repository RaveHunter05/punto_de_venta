from django.shortcuts import render
from .models import Post

# Create your views here.

#CRUD - create, retrieve, update, delete

#List all the posts in a view

def post_list_view(request):
    post_objects = Post.objects.all()
    context = {
        'post_objects': post_objects
    }
    return render(request, "posts/index.html", context)
