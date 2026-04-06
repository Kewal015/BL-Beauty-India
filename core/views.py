from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def products(request):
    return render(request, 'products.html')


def gallery(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')
