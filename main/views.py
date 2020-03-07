from django.shortcuts import render

# Create your views here.
def mainPage(request, category_slug=None):
    return render(request, 'pages/main.html')
def aboutPage(request, category_slug=None):
    return render(request, 'pages/about_us.html')
def blogPage(request, category_slug=None):
    return render(request, 'pages/blog.html')
def pricesPage(request, category_slug=None):
    return render(request, 'pages/prices.html')
def contactsPage(request, category_slug=None):
    return render(request, 'pages/contacts.html')