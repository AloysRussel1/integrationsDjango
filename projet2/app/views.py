from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def practices(request):
    return render(request, 'practices.html')

def lawyers(request):
    return render(request, 'lawyers.html')

def news(request):
    return render(request, 'news.html')

def contact(request):
    return render(request, 'contact.html')

def singlepost(request):
    return render(request, 'singlepost.html')

def post(request):
    return render(request, 'post.html')

