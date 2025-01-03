from django import forms

from .models import STATE_CHOICES, FURNISHING_CHOICES, HEATING_CHOICES, Condition, Content


class AdForm(forms.Form):
    num_of_rooms     = forms.IntegerField(label="Broj soba", min_value=0, max_value=6, initial=1, required=True)
    location         = forms.CharField(max_length=32, label="Lokacija", required=True)
    price            = forms.IntegerField(label="Cena", initial=0, required=True)
    area             = forms.IntegerField(label="Kvadratura", initial=0, required=True)
    story            = forms.IntegerField(label="Sprat", min_value=0, initial=0, required=True)
    state            = forms.ChoiceField(choices=STATE_CHOICES, label="Stanje", initial="OG", required=True)
    furnishing       = forms.ChoiceField(choices=FURNISHING_CHOICES, label="Nameštenost", initial="FU", required=True)
    heating          = forms.ChoiceField(choices=HEATING_CHOICES, label="Grejanje", initial="DI", required=True)
    conditions  = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Condition.objects.all(), label="Uslovi", required=True)
    contents    = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Content.objects.all(), label="Sadržaj", required=True)
    title            = forms.CharField(max_length=64, label="Naslov", required=True)
    description      = forms.CharField(widget=forms.Textarea(attrs={
        "rows": "5",
        "cols": "50",
        "placeholder": "Napišite tekst ovde"
    }), label="Opis", required=True)
    has_images       = forms.BooleanField(label="Ima slike", required=True)
    move_date        = forms.DateField(widget=forms.DateInput(attrs={
        "type": "date"
    }), label="Datum useljenja", required=True)