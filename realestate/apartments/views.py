from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Ad, Apartment
from .forms import AddForm, SearchForm

# Create your views here.
def index(request):
    ads = Ad.objects.all()
    
    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            filters = {
                "apartment__num_of_rooms": form.cleaned_data["num_of_rooms"],
                "apartment__location":     form.cleaned_data["location"],
                "apartment__price":        form.cleaned_data["price"],
                "apartment__area":         form.cleaned_data["area"],
                "apartment__story":        form.cleaned_data["story"],
                "apartment__state":        form.cleaned_data["state"],
                "apartment__furnishing":   form.cleaned_data["furnishing"],
                "apartment__heating":      form.cleaned_data["heating"],
            }

            for field, value in filters.items():
                if value:
                    ads = ads.filter(**{field: value})
                
            if conditions := form.cleaned_data["conditions"]:
                ads = ads.filter(apartment__conditions__in=conditions)

            if contents := form.cleaned_data["contents"]:
                ads = ads.filter(apartment__contents__in=contents)
    else:
        form = SearchForm()

    return render(request, "apartments/index.html", { "form": form, "ads": ads })


def search(request):
    return render(request, "apartments/search.html")


def detail(request, id):
    ad = Ad.objects.get(pk=id)
    return render(request, "apartments/detail.html", { "ad": ad })


def add(request):
     if request.method == "POST":
        form = AddForm(request.POST)

        if form.is_valid():
            apartment, created = Apartment.objects.get_or_create(
                num_of_rooms=form.cleaned_data["num_of_rooms"],
                location=    form.cleaned_data["location"],
                price=       form.cleaned_data["price"],
                area=        form.cleaned_data["area"],
                story=       form.cleaned_data["story"],
                state=       form.cleaned_data["state"],
                furnishing=  form.cleaned_data["furnishing"],
                heating=     form.cleaned_data["heating"]
            )
            apartment.conditions.set(form.cleaned_data["conditions"])
            apartment.contents.set(form.cleaned_data["contents"])
            ad = Ad(
                title=       form.cleaned_data["title"],
                description= form.cleaned_data["description"],
                date_updated=None,
                has_images=  False,
                move_date=   form.cleaned_data["move_date"],
                apartment=   apartment
            )
            ad.save()
            return HttpResponseRedirect(reverse("index"))
     else:
        form = AddForm()
        return render(request, "apartments/add.html", { "form": form })