from django.urls import path
from .views import BlogView
from . import views

urlpatterns = [
    path('', BlogView.as_view(), name="blog"),
    path('category/<int:category_id>/', views.category, name="category"),
]