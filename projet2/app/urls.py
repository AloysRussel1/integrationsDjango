from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('lawyers/', views.lawyers, name='lawyers'),
    path('news/', views.news, name='news'),
    path('singlepost/', views.singlepost, name='singlepost'),
    path('practices/', views.practices, name='practices'),
    path('post/', views.post, name='post'),
]