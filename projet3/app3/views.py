from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')


def classes(request):
    return render(request, 'classes.html')


def videos(request):
    return render(request, 'videos.html')


def membership(request):
    return render(request, 'membership.html')


def services(request):
    return render(request, 'services.html')
