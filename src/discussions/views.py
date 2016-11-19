from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from discussions.forms import SearchForm
from discussions.models import Post
from django.views.generic import ListView, CreateView, UpdateView, DetailView

class PostListAjax(ListView):
    template_name = 'discussions/ajax_list.html'
    context_object_name = 'latest_posts_list'
    model = Post

    def get_queryset(self):
        return Post.objects.all()




from .models import Post

# def course_view(request, *args, **kwargs):
#     print(request, args, kwargs)

class PostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'discussions/discussion.html'


