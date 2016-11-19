from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from discussions.forms import SearchForm
from discussions.models import Post


class PostListAjax(ListView):
    template_name = 'discussions/ajax_list.html'
    context_object_name = 'latest_posts_list'
    model = Post

    def get_queryset(self):
        return Post.objects.all()

