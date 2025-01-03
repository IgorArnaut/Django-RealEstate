from django import forms

from .models import STATE_CHOICES, FURNISHING_CHOICES, HEATING_CHOICES, Condition, Content


class AddForm(forms.Form):
    num_of_rooms = forms.IntegerField(label="Broj soba", min_value=0, max_value=6, initial=1)
    location     = forms.CharField(max_length=32, label="Lokacija")
    price        = forms.IntegerField(label="Cena", initial=0)
    area         = forms.IntegerField(label="Kvadratura", initial=0)
    story        = forms.IntegerField(label="Sprat", min_value=0, initial=0)
    state        = forms.ChoiceField(choices=STATE_CHOICES, label="Stanje", initial="OG")
    furnishing   = forms.ChoiceField(choices=FURNISHING_CHOICES, label="Nameštenost", initial="FU")
    heating      = forms.ChoiceField(choices=HEATING_CHOICES, label="Grejanje", initial="DI")
    conditions   = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Condition.objects.all(), label="Uslovi")
    contents     = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Content.objects.all(), label="Sadržaj")
    title        = forms.CharField(max_length=64, label="Naslov")
    description  = forms.CharField(widget=forms.Textarea(attrs={
        "rows": "5",
        "cols": "50",
        "placeholder": "Napišite tekst ovde"
    }), label="Opis")
    has_images   = forms.BooleanField(label="Ima slike")
    move_date    = forms.DateField(widget=forms.DateInput(attrs={ "type": "date" }), label="Datum useljenja")


class SearchForm(forms.Form):
    num_of_rooms = forms.IntegerField(label="Broj soba", min_value=0, max_value=6, required=False)
    location     = forms.CharField(max_length=32, label="Lokacija", required=False)
    price        = forms.IntegerField(label="Cena", required=False)
    area         = forms.IntegerField(label="Kvadratura", required=False)
    story        = forms.IntegerField(label="Sprat", min_value=0, required=False)
    state        = forms.ChoiceField(choices={None: "----", **STATE_CHOICES}, label="Stanje", required=False)
    furnishing   = forms.ChoiceField(choices={None: "----", **FURNISHING_CHOICES}, label="Nameštenost", required=False)
    heating      = forms.ChoiceField(choices={None: "----", **HEATING_CHOICES}, label="Grejanje", required=False)
    conditions   = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Condition.objects.all(), label="Uslovi", required=False)
    contents     = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Content.objects.all(), label="Sadržaj", required=False)