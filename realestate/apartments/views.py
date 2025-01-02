from django.shortcuts import render

from .models import Ad

# Create your views here.
def index(request):
    ads = Ad.objects.all()
    context = {
        'ads': ads
    }
    return render(request, 'apartments/index.html', context)


def search(request):
    return render(request, 'apartments/search.html')


def detail(request, id):
    ad = Ad.objects.get(pk=id)
    return render(request, 'apartments/detail.html', { 'ad': ad })