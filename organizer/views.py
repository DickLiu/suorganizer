#from django.http.response import (HttpResponse, Http404)
#from django.template import RequestContext, loader
from .models import  Tag, Startup
from django.shortcuts import (get_object_or_404, render, redirect)
from .forms import TagForm
from django.views.generic import View
from .utils import ObjectCreateMixin
# Create your views here.

def tag_list(request):
    return render(request, 'organizer/tag_list.html', {'tag_list':Tag.objects.all()})        
    
def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug) #replace try...except block
    return render(request, 'organizer/tag_detail.html', {'tag':tag}) #replace render_to_response method

class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'
    def get(self, request):
        return render(request,
                      self.template_name,
                      {'form':self.form_class()})
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        else:
            render(request, self.template_name, {'form':bound_form})
    
def startup_list(request):
    return render(
        request, 
        'organizer/startup_list.html', 
        {'startup_list':Startup.objects.all()})
    
def startup_detail(request, slug):
    startup = get_object_or_404(
        Startup, slug__iexact=slug)
    return render(request, 
    'organizer/startup_detail.html',
    {'startup':startup})

class StartupCreate(ObjectCreateMixin, View):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'
    def get(self, request):
        return render(request, self.template_name, {'form':self.form_class()})
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_startup = bound_form.save()
            return redirect(new_startup)
        else:
            return render(request, self.template_name, {'form':bound_form})
            
class NewsLinkCreate(ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template_name = 'organizer/newlink_form.html'
    def get(self, request):
        return render(request, self.template_name, {'form':self.form_class()})
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            return render(request, self.template_name, {'form':bound_form})
    