from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
path('details/', views.details, name='details'),




    path('resume/', views.resume, name='resume'),
]
