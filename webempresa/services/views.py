from django.shortcuts import render#, render_to_response
from django.views.generic.list import ListView
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from .models import Service
# Create your views here.

'''def services(request): 
    services = Service.objects.all() 
    paginator = Paginator(services, 1) # Show 25 contacts per page 

    page = request.GET.get('page') 
    try: 
        servicios = paginator.page(page) 
    except PageNotAnInteger: 
        # If the page is not an integer, deliver the first page. 
        servicios = paginator.page(1) 
    except EmptyPage: 
        # If the page is out of range (for example, 9999), deliver the last page of results.
        servicios = paginator.page(pager.num_pages) 

    return render_to_response('services/services.html', {'services':services})'''
class ServicesView(ListView):
    model = Service 
    template_name = "services/services.html" 
    context_object_name = "obj"  
    paginate_by = 10
    

    