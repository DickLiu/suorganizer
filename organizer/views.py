#from django.http.response import (HttpResponse, Http404)
#from django.template import RequestContext, loader
from django.core.urlresolvers import reverse_lazy, reverse
from .models import  (Tag, Startup, NewsLink)
from django.shortcuts import (get_object_or_404, render, redirect)
from .forms import (TagForm, StartupForm, NewsLinkForm)
from django.views.generic import (View, 
                                  DetailView,
                                  CreateView,
                                  DeleteView,
                                  ListView,)
from core.utils import UpdateView
from .utils import PageLinksMixin
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
# Create your views here.

class TagList(PageLinkMixin,ListView):
    paginate_by = 5
    model = Tag
print(TagList, __mro__)

class TagDetail(DetailView):
    model = Tag
        
class StartupList(PageLinkMixin,ListView):
    model = Startup
    paginate_by = 5
    
    
class StartupDetail(DetailView):
    form_class = StartupForm
    model = Startup

class StartupCreate(CreateView):
    form_class = StartupForm
    model = Startup
            
class NewsLinkCreate(CreateView):
    form_class = NewsLinkForm
    model = NewsLink

class TagCreate(CreateView):
    form_class = TagForm
    model = Tag
    
class NewsLinkUpdate(UpdateView):
    form_class  = NewsLinkForm
    model = NewsLink
    template_name_suffix = '_form_update'

                          
class TagUpdate(UpdateView):
    form_class = TagForm
    template_name_suffix = '_form_update'
    model = Tag
    
class StartupUpdate(UpdateView):
    form_class = StartupForm
    template_name_suffix= '_form_update'
    model = Startup
    
class NewsLinkDelete(DeleteView):
    model = NewsLink
    def get_success_url(self):
        return (self.object.startup
                .get_absolute_url())

class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('organizer_tag_list') 
    #因為此時Django尚未載入urlconf，使用reverse()會出錯
    
class StartupDelete(DeleteView):
    model = Startup
    success_url = reverse_lazy('organizer_startup_list')

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
    
    
    
    
                                      
    

    