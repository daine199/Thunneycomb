
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views import generic
from .models import Article, Comment

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'dance_eight/index.html'
    context_object_name = ''

    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Article
    template_name = 'dance_eight/detail.html'


