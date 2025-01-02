from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Ad
from .forms import AdForm

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


def add(request):
     if request.method == 'POST':
        form = AdForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect(reverse('index'))
     else:
        form = AdForm()
        return render(request, 'apartments/add.html', { 'form': form })