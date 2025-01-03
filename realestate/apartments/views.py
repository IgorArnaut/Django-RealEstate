from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Ad, Apartment
from .forms import AdForm

# Create your views here.
def index(request):
    ads = Ad.objects.all()
    context = {
        "ads": ads
    }
    return render(request, "apartments/index.html", context)


def search(request):
    return render(request, "apartments/search.html")


def detail(request, id):
    ad = Ad.objects.get(pk=id)
    return render(request, "apartments/detail.html", { "ad": ad })


def add(request):
     if request.method == "POST":
        form = AdForm(request.POST)

        if form.is_valid():
            apartment, created = Apartment.objects.get_or_create(
                num_of_rooms=form.cleaned_data["num_of_rooms"],
                location=form.cleaned_data["location"],
                price=form.cleaned_data["price"],
                area=form.cleaned_data["area"],
                story=form.cleaned_data["story"],
                state=form.cleaned_data["state"],
                furnishing=form.cleaned_data["furnishing"],
                heating=form.cleaned_data["heating"],
            )
            apartment.conditions.set(form.cleaned_data["conditions"])
            apartment.contents.set(form.cleaned_data["contents"])
            ad = Ad(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                date_updated=None,
                has_images=False,
                move_date=form.cleaned_data["move_date"],
                apartment=apartment
            )
            ad.save()
            return HttpResponseRedirect(reverse("index"))
     else:
        form = AdForm()
        return render(request, "apartments/add.html", { "form": form })