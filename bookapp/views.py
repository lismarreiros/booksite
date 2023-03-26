from django.shortcuts import render
from .models import Book

# Create your views here.
def home(request):
    recommended_books= Book.objects.filter(recommended_books = True)
    fiction_books= Book.objects.filter(fiction_books = True)
    business_books= Book.objects.filter(business_books = True)
    launch_books= Book.objects.filter(launch_books = True)
    return render(request, 'home.html', {'recommended_books' : recommended_books, 'business_books': business_books, 'fiction_books': fiction_books, 'launch_books': launch_books })

def search_book(request):
    searched_books = Book.objects.filter(title__icontains = request.POST.get('name_of_book'))
    return render(request, 'search_book.html', {'searched_books': searched_books})