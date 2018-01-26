from django import forms
from app.models import *


class EventForm(forms.ModelForm):
    class Meta:
        model = Wydarzenie
        fields = ('nazwa', 'opis', 'data', 'budynek')


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('zglaszajacy', 'opis')


class BudynekForm(forms.ModelForm):
    class Meta:
        model = Budynek
        fields = ('adres', 'administrator')


class PracownikForm(forms.ModelForm):
    class Meta:
        model = Pracownik
        fields = ('stanowisko', 'budynek', 'imie', 'nazwisko', 'telefon', 'email', 'adres')


class StanowiskoForm(forms.ModelForm):
    class Meta:
        model = Stanowisko
        fields = ('nazwa', 'pensja')


class AdresBudynekForm(forms.ModelForm):
    class Meta:
        model = AdresBudynek
        fields = ('kod_pocztowy', 'miasto', 'ulica')


class AdresForm(forms.ModelForm):
    class Meta:
        model = Adres
        fields = ('kod_pocztowy', 'miasto', 'ulica')


class WystawcaForm(forms.ModelForm):
    class Meta:
        model = Wystawca
        fields = ('nazwa', 'kod_pocztowy', 'miasto', 'ulica', 'telefon', 'email')


class FakturaForm(forms.ModelForm):
    class Meta:
        model = Faktura
        fields = ('wartosc_netto', 'wystawca', 'wlasciciel')


class LicznikForm(forms.ModelForm):
    class Meta:
        model = Licznik
        fields = ('typ', 'cena_netto')


class StanLicznikForm(forms.ModelForm):
    class Meta:
        model = StanLicznik
        fields = ('typ', 'mieszkanie', 'stan')


class NadgodzinyForm(forms.ModelForm):
    class Meta:
        model = Nadgodziny
        fields = ('pracownik', 'ilosc')


class MieszkanieForm(forms.ModelForm):
    class Meta:
        model = Mieszkanie
        fields = ('budynek', 'metraz', 'liczba_pokoi', 'piwnica', 'nr_mieszkania')


class WlascicielForm(forms.ModelForm):
    class Meta:
        model = Wlasciciel
        fields = ('imie', 'nazwisko', 'telefon', 'email', 'mieszkanie')
