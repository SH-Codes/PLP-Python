from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html', name)
    name = {
        "first_name": "Sihle",
    }

def about_view(request):
    return render(request, 'about.html')

def menu_view(request):
    return render(request, 'menu.html')

def book_view(request):
    return render(request, 'book.html')