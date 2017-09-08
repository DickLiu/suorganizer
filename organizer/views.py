#from django.http.response import (HttpResponse, Http404)
#from django.template import RequestContext, loader
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from django.shortcuts import (get_object_or_404, render, redirect)
from django.views.generic import (View, 
                                  DetailView,
                                  CreateView,
                                  DeleteView,
                                  ListView,)
from django.contrib.auth.decorators import (
                                  login_required,
                                  permission_required)
from django.contrib.auth import PermissionDenied
from django.utils.decorators import method_decorator
from core.utils import UpdateView

from .utils import (NewsLinkGetObjectMixin,
                    StartupContextMixin,
                    PageLinksMixin,
                    StartupContextMixin,)
from .models import  (Tag, Startup, NewsLink)
from .forms import (TagForm, StartupForm, NewsLinkForm)
from user.decorators import custom_login_required

def model_list(request, model):
    context_object_name = '{}_list'.format(
        model._meta.model_name)
    context={
        context_object_name:model.objects.all(),}
    template_name=(
        'organizer/{}_list.html'.format(
            model._meta.model_name))
    return render(
        request, template_name, context)
    
class TagList(PageLinksMixin,ListView):
    paginate_by = 5
    model = Tag

class TagDetail(DetailView):
    model = Tag

class TagCreate(CreateView):
    form_class = TagForm
    model = Tag
    
    @method_decorator(custom_login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(
                request, *args, **kwargs)
    
class TagUpdate(UpdateView):
    form_class = TagForm
    template_name_suffix = '_form_update'
    model = Tag
    
class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('organizer_tag_list') 
    #因為此時Django尚未載入urlconf，使用reverse()會出錯
        
class StartupList(PageLinksMixin,ListView):
    model = Startup
    paginate_by = 5    
    
class StartupDetail(DetailView):
    form_class = StartupForm
    model = Startup

class StartupCreate(CreateView):
    form_class = StartupForm
    model = Startup

class StartupUpdate(UpdateView):
    form_class = StartupForm
    template_name_suffix= '_form_update'
    model = Startup

class StartupDelete(DeleteView):
    model = Startup
    success_url = reverse_lazy('organizer_startup_list')
            
class NewsLinkCreate(
        NewsLinkGetObjectMixin,
        StartupContextMixin,
        CreateView):
    form_class = NewsLinkForm
    model = NewsLink
    
    def get_initial(self):
        startup_slug = self.kwargs.get(
                self.startup_slug_url_kwarg)
        self.startup = get_object_or_404(
                Startup, slug__iexact=startup_slug)
        initial = {
                self.startup_context_object_name:
                    self.startup,}
        initial.update(self.initial)
        return initial
    
class NewsLinkUpdate(
        NewsLinkGetObjectMixin,
        StartupContextMixin,
        UpdateView,):
    form_class  = NewsLinkForm
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'
        
class NewsLinkDelete(        
        StartupContextMixin,
        DeleteView,):
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'
    
    def get_success_url(self):
        return (self.object.startup
                .get_absolute_url())


    
    
    
    
                                      
    

    