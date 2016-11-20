from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from django.views.generic import CreateView, DetailView
from django.views.generic import ListView
from django.contrib.contenttypes.models import ContentType
from application.settings import LOGIN_URL

from comments.models import Comment
from courses.models import Course
from discussions.forms import SearchForm, CommentForm
from discussions.models import Post
from django.http import HttpResponseRedirect
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import reverse

class DocsDetail(DetailView):
    pass

class DocsListAjax(ListView):
    pass
