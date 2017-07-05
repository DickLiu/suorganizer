from django.shortcuts import (render, get_object_or_404, redirect)
from django.core.urlresolvers import reverse_lazy
from .models import Post
from django.views.generic import (View,
                                  ArchiveIndexView,
                                  CreateView,
                                  DateDetailView,
                                  YearArchiveView,
                                  MonthArchiveView,
                                  DetailView,)
from .utils import PostGetMixin
from .forms import PostForm
from core.utils import UpdateView


class PostList(ArchiveIndexView):
    allow_empty = True
    allow_future = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    model = Post
    paginate_by = 5
    template_name = 'blog/post_list.html'

class PostDetail(PostGetMixin, DetailView):
    model = Post
    
class PostCreate(CreateView):
    form_class = PostForm
    model = Post
        
class PostUpdate(PostGetMixin, UpdateView):
    form_class = PostForm
    model = Post
            
class PostDelete(PostGetMixin, DeleteView):
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
        
    