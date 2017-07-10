from django.shortcuts import (render, get_object_or_404, redirect)
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View,
                                  ArchiveIndexView,
                                  CreateView,
                                  DateDetailView,
                                  YearArchiveView,
                                  MonthArchiveView,
                                  DetailView,)

from core.utils import UpdateView

from .utils import DateObjectMixin
from .forms import PostForm
from .models import Post



class PostList(ArchiveIndexView):
    allow_empty = True
    allow_future = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    model = Post
    paginate_by = 5
    template_name = 'blog/post_list.html'

class PostDetail(DateObjectMixin, DetailView):
    allow_future = True
    date_field = 'pub_date'
    model = Post
    
class PostCreate(CreateView):
    form_class = PostForm
    model = Post
        
class PostUpdate(DateObjectMixin, UpdateView):
    allow_future = True
    date_field = 'pub_date'    
    form_class = PostForm
    model = Post
            
class PostDelete(DateObjectMixin, DeleteView):
    allow_future = True
    date_field = 'pub_date'    
    model = Post
    success_url = reverse_lazy('blog_post_list')

class PostArchiveYear(YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True
    
class PostArchiveMonth(MonthArchiveView):
    model= Post
    date_field = 'pub_date'
    month_format = '%m'
        
    