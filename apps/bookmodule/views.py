from django.shortcuts import render, redirect

def index(request):
    # study the request ,,,,
    return render(request, 'bookmodule/index.html') # rendering a template

def books(request):
    return render(request, 'bookmodule/bookList.html')  # we need a request
    #return redirect('/') # we need just the root

def book(request, bId):
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 5678865, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    
    targetBook = None
    if book1['id'] == bId: targetBook = book1
    if book2['id'] == bId: targetBook = book2

    if targetBook == None: return redirect('/books')
    
    context = {'book': targetBook} # book is the variable accessible by template
    return render(request, 'bookmodule/book.html', context)