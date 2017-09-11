from django.shortcuts import (render, get_object_or_404, redirect)
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View,
                                  ArchiveIndexView,
                                  CreateView,
                                  DateDetailView,
                                  YearArchiveView,
                                  MonthArchiveView,
                                  DetailView,
                                  DeleteView)

from core.utils import UpdateView

from .utils import (DateObjectMixin, 
                    AllowFuturePermissionMixin)
from .forms import PostForm
from .models import Post

from user.decorators import require_authenticated_permission



class PostList(
        AllowFuturePermissionMixin,
        ArchiveIndexView):
    allow_empty = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    model = Post
    paginate_by = 5
    template_name = 'blog/post_list.html'


class PostDetail(DateObjectMixin, DetailView):
    date_field = 'pub_date'
    model = Post

@require_authenticated_permission(
        'blog.add_post')
class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    
@require_authenticated_permission(
        'blog.change_post')
class PostUpdate(DateObjectMixin, UpdateView):
    date_field = 'pub_date'    
    form_class = PostForm
    model = Post

@require_authenticated_permission(
        'blog.delete_post')
class PostDelete(DateObjectMixin, DeleteView):
    date_field = 'pub_date'    
    model = Post
    success_url = reverse_lazy('blog_post_list')

class PostArchiveYear(
        AllowFuturePermissionMixin,
        YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True
    
class PostArchiveMonth(        
        AllowFuturePermissionMixin,
        MonthArchiveView):
    model= Post
    date_field = 'pub_date'
    month_format = '%m'
        
    