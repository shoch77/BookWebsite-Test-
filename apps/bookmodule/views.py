from django.shortcuts import render

def index(request):
    # study the request
    return render(request, 'bookmodule/index.html') # rendering a template