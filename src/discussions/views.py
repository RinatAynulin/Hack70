from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import CreateView
from django.views.generic import ListView

from comments.models import Comment
from discussions.forms import SearchForm
from discussions.models import Post


class PostListAjax(ListView):
    template_name = 'discussions/ajax_list.html'
    context_object_name = 'latest_posts_list'
    model = Post

    def get_queryset(self):
        return Post.objects.all()


class PostDetail(CreateView):
    model = Comment
    template_name = 'discussions/detail.html'
    fields = ('content',)

    def dispatch(self, request, pk=None, *args, **kwargs):
        # when I used name 'post' instead of 'current_post', it rewrited field post (it's post request),
        # and some **it happened
        self.current_post = get_object_or_404(Post, id=pk)
        return super(PostDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['post'] = self.current_post
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = self.current_post
        return super(PostDetail, self).form_valid(form)

    def get_success_url(self):
        return '.'