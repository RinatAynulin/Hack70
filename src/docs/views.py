from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from django.views.generic import CreateView, DetailView
from django.views.generic import ListView
from django.contrib.contenttypes.models import ContentType
from application.settings import LOGIN_URL

from comments.models import Comment
from courses.models import Course
from .forms import SearchForm, CommentForm
from .models import Document
from django.http import HttpResponseRedirect
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import reverse


class DocsListAjax(ListView):
    model = Document
    template_name = 'docs/ajax_list.html'
    context_object_name = 'latest_docs_list'

    def get_queryset(self):
        return Course.objects.get(slug=self.kwargs['course_slug']).course_docs.all()

class DocDetail(DetailView):
    model = Document
    context_object_name = 'doc'
    template_name = 'docs/docs.html'
    success_url = '.'

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.user = request.user
        self.comment_form = CommentForm
        return super(DocDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DocDetail, self).get_context_data(**kwargs)
        context['comment_form'] = self.comment_form
        return context

    def get_queryset(self):
        return Document.objects.filter(course__slug=self.kwargs['course_slug']).filter(course__chair__slug=self.kwargs['chair_slug'])

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.comment_form(request.POST)
        if request.user.is_anonymous():
            return redirect_to_login(next=reverse('courses:docs', args=[str(self.object.course.chair.slug),
                                                                                str(self.object.course.slug),str(self.object.pk)]), login_url=LOGIN_URL)
        if form.is_valid():
            comment = Comment()
            comment.author = request.user
            comment.text = form.cleaned_data['comment']
            comment.content_type = ContentType.objects.get_for_model(self.model)
            comment.object_id = self.object.pk
            comment.save()
        return HttpResponseRedirect(self.success_url)
