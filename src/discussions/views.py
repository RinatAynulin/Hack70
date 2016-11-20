from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import CreateView, DetailView
from django.views.generic import ListView
from django.contrib.contenttypes.models import ContentType
from application.settings import LOGIN_URL

from comments.models import Comment
from courses.models import Course
from discussions.forms import SearchForm, CommentForm
from discussions.models import Post, News
from django.http import HttpResponseRedirect
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import reverse


class PostListAjax(ListView):
    model = Post
    template_name = 'discussions/ajax_list.html'
    context_object_name = 'latest_posts_list'

    def get_queryset(self):
        return Course.objects.get(slug=self.kwargs['course_slug']).course_posts.all()


class NewsListAjax(ListView):
    model = News
    template_name = 'discussions/news_ajax_list.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
        return Course.objects.get(slug=self.kwargs['course_slug']).course_news.all()

class PostDetail(DetailView):
    model = Post
    context_object_name = 'current_post'
    template_name = 'discussions/test.html'
    # fields = ('content',)
    success_url = '.'

    def dispatch(self, request, pk=None, *args, **kwargs):
        # when I used name 'post' instead of 'current_post', it rewrited field post (it's post request),
        # and some **it happened
        # self.current_post = get_object_or_404(Post, id=pk)
        # return super(PostDetail, self).dispatch(request, *args, **kwargs)

        self.user = request.user
        self.comment_form = CommentForm
        return super(PostDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['comment_form'] = self.comment_form
        return context

    def get_queryset(self):
        return Post.objects.filter(course__slug=self.kwargs['course_slug']).filter(course__chair__slug=self.kwargs['chair_slug'])

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.comment_form(request.POST)
        if request.user.is_anonymous():
            #TODO
            return redirect_to_login(next=reverse('courses:discussion', args=[str(self.object.course.chair.slug),
                                                                                str(self.object.course.slug),str(self.object.pk)]), login_url=LOGIN_URL)
        if form.is_valid():
            comment = Comment()
            comment.author = request.user
            comment.text = form.cleaned_data['comment']
            comment.content_type = ContentType.objects.get_for_model(self.model)
            comment.object_id = self.object.pk
            comment.save()
        return HttpResponseRedirect(self.success_url)

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     form.instance.post = self.current_post
    #     return super(PostDetail, self).form_valid(form)
    #
    # def get_success_url(self):
    #     return '.'