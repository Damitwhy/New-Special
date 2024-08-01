from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'list_app/index.html')

def about(request):
    return render(request, 'list_app/about.html')

def contact(request):
    return render(request, 'list_app/contacts.html')

def dash(request):
    return render(request, 'list_app/dash.html')
