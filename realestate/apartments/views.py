from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'apartments/index.html')


def search(request):
    return render(request, 'apartments/search.html')