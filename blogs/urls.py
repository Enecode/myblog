from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('project/', views.projects, name="project"),
    path('post_list/', views.post_list, name="post_list"),
    path('<slug:post>/', views.post_detail, name="post_detail"),

]
