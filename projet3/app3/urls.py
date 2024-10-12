from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('classes/', views.classes, name='classes'),
    path('videos/', views.videos, name='videos'),
    path('membership/', views.membership, name='membership'),
    path('services/', views.services, name='services'),
    
]