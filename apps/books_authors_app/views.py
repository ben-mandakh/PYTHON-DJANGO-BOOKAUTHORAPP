from django.shortcuts import render, redirect
from .models import Book
from .models import Author

def index(request):                
    context = {"books": Book.objects.all()}
    return render(request, "books_authors_app/index.html", context)                                

def input(request):
    Book.objects.create(title=request.POST['title'], desc = request.POST['desc'])
    return redirect ("/") 