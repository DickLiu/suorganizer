#from django.http.response import (HttpResponse, Http404)
#from django.template import RequestContext, loader
from .models import  Tag, Startup
from django.shortcuts import (get_object_or_404, render)
# Create your views here.

def tag_list(request):
#    tag_list = Tag.objects.all()
#    template = loader.get_template('organizer/tag_list.html')
#    context = RequestContext(request, {'tag_list':tag_list})
#    output = template.render(context)
#    return HttpResponse(output)
#    return render_to_response('organizer/tag_list.html',{'tag_list':Tag.objects.all()})
    return render(request, 'organizer/tag_list.html', {'tag_list':Tag.objects.all()})        
    
def tag_detail(request, slug):
#    # slug = ?
##    try:
##        tag = Tag.objects.get(slug__iexact=slug)
##    except Tag.DoesNotExist:
##        raise Http404
    tag = get_object_or_404(Tag, slug__iexact=slug) #replace try...except block
#    template = loader.get_template('organizer/tag_detail.html')
#    context = RequestContext(request, {'tag':tag})
#    return HttpResponse(template.render(context))
    return render(request, 'organizer/tag_detail.html', {'tag':tag}) #replace render_to_response method
    
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