from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Post, Category

# Create your views here.

'''def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts':posts})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category':category})'''

class BlogView(ListView):
    model = Post 
    template_name = "blog/blog.html" 
    context_object_name = "obj"  
    paginate_by = 10

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category':category})


'''class CategoryView(ListView):
    model = Category 
    template_name = "blog/category.html" 
    context_object_name = "obj"  
    paginate_by = 6'''
