#from django.http.response import (HttpResponse, Http404)
#from django.template import RequestContext, loader
from django.core.urlresolvers import reverse_lazy, reverse
from .models import  (Tag, Startup, NewsLink)
from django.shortcuts import (get_object_or_404, render, redirect)
from .forms import (TagForm, StartupForm, NewsLinkForm)
from django.views.generic import View
from .utils import (ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin)
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
# Create your views here.

class TagList(View):
    template_name='organizer/tag_list.html'
    def get(self, request):
        tags = Tag.objects.all()
        context = {'tag_list':tags}
        return render(request, 
                      self.template_name, 
                      context)

class TagPageList(View):
    paginate_by = 5
    template_name='organizer/tag_list.html'
    def get(self, request, page_number):
        tags = Tag.objects.all()
        paginator = Paginator(tags, self.paginate_by)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(
            paginator.num_pages)
        if page.has_previous():
            prev_url = reverse(
            'organizer_tag_page',
            args=(page.previous_page_number(),
                  ))
        else:
            prev_url = None
        if page.has_next():
            next_url = reverse(
            'organizer_tag_page',
            args=(page.next_page_number(),
                  ))
        else:
            next_url = None
        context ={
        'is_paginated':page.has_other_pages(),
        'next_page_url':next_url,
        'paginator':paginator,
        'previous_page_url':prev_url,
        'tag_list':page}
        return render(request, self.template_name,
                      context)
        
        
    
def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug) #replace try...except block
    return render(request, 'organizer/tag_detail.html', {'tag':tag}) #replace render_to_response method
   
        
class Startup_List(View):
    page_kwarg = 'page'    
    paginate_by = 5
    template_name = 'organizer/startup_list.html'
    def get(self, request):
        startups = Startup.objects.all()
        paginator = Paginator(startups,
                              self.paginate_by)
        page_number = request.GET.get(self.page_kwarg)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        if page.has_previous():
            prev_url = '?{pkw}={n}'.format(
            pkw=self.page_kwarg,
            n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = '?{pkw}={n}'.format(
            pkw=self.page_kwarg,
            n=page.next_page_number())
        else:
            next_url = None
        context = {
        'startup_list':page,
        'paginator':paginator,
        'is_paginated':page.has_other_pages(),
        'next_page_url':next_url,
        'previous_page_url':prev_url}
        return render(request,
                      self.template_name,
                      context)
    
def startup_detail(request, slug):
    startup = get_object_or_404(
        Startup, slug__iexact=slug)
    return render(request, 
    'organizer/startup_detail.html',
    {'startup':startup})

class StartupCreate(ObjectCreateMixin, View):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'
            
class NewsLinkCreate(ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template_name = 'organizer/newlink_form.html'

class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'
    
class NewsLinkUpdate(View):
    form_class  = NewsLinkForm
    template_name = 'organizer/newslink_form_update.html'
    def get(self, request, pk):
        newslink = get_object_or_404(NewsLink,
                                     pk=pk)
        context = {'form':self.form_class(instance=newslink),
                   'newslink':newslink,}
        return render(request,
                      self.template_name,
                      context)
    def post(self, request, pk):
        newslink = get_object_or_404(NewsLink,
                                     pk=pk)
        bound_form = self.form_class(request.POST,
                                     instance=newslink)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            context = {'form':bound_form,
                       'newslink':newslink,}
            return render(request,
                          self.template_name,
                          context)
                          
class TagUpdate(ObjectUpdateMixin, View):
    form_class = TagForm
    template_name = 'organizer/tag_form_update.html'
    model = Tag
    
class StartupUpdate(ObjectUpdateMixin, View):
    form_class = StartupForm
    template_name= 'organizer/startup_form_update.html'
    model = Startup
    
class NewsLinkDelete(View):
    template_name = 'organzier/newslink_confirm_delete.html'
    def get(self, pk):
        newslink = get_object_or_404(NewsLink,
                                     pk = pk)
        return render(request, 
                      template_name,
                      {'newslink':newslink})
    def post(self, pk):
        newslink = get_object_or_404(NewsLink,
                                     pk = pk)
        startup = newslink.startup
        newslink.delete()
        return redirect(startup)

class TagDelete(ObjectDeleteMixin, View):
    template_name = 'organizer/tag_confirm_delete.html'
    model = Tag
    success_url = reverse_lazy('organizer_tag_list') 
    #因為此時Django尚未載入urlconf，使用reverse()會出錯
class StartupDelete(ObjectDeleteMixin, View):
    template_name = 'organizer/startup_confirm_delete.html'
    model = Startup
    success_url = reverse_lazy('organizer_startup_list')
    
    
    
                                      
    

    