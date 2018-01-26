from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group


class Adres(models.Model):
    id = models.AutoField(primary_key=True)
    kod_pocztowy = models.TextField()
    miasto = models.TextField()
    ulica = models.TextField()

    class Meta:
        db_table = 'adres'


class AdresBudynek(models.Model):
    id = models.AutoField(primary_key=True)
    kod_pocztowy = models.TextField()
    miasto = models.TextField()
    ulica = models.TextField()

    class Meta:
        db_table = 'adresbudynek'


class Budynek(models.Model):
    id = models.AutoField(primary_key=True)
    adres = models.ForeignKey('AdresBudynek', models.SET('usunieto'), db_column='adresbudynek', related_name='+')
    administrator = models.ForeignKey('Pracownik', models.SET('usunieto'), db_column='administrator', related_name='+')

    class Meta:
        db_table = 'budynek'


class Faktura(models.Model):
    id = models.AutoField(primary_key=True)
    wartosc_netto = models.FloatField()
    wystawca = models.ForeignKey('Wystawca', models.SET('usunieto'), db_column='wystawca', related_name='+')
    wlasciciel = models.ForeignKey('Wlasciciel', models.SET('usunieto'), db_column='wlasciciel', null=True, blank=True, related_name='+')

    class Meta:
        db_table = 'faktura'


class Mieszkanie(models.Model):
    id = models.AutoField(primary_key=True)
    budynek = models.ForeignKey('Budynek', models.SET('usunieto'), db_column='budynek', related_name='+')
    metraz = models.FloatField()
    liczba_pokoi = models.IntegerField()
    piwnica = models.BooleanField()
    nr_mieszkania = models.IntegerField()

    class Meta:
        db_table = 'mieszkanie'


class Nadgodziny(models.Model):
    id = models.AutoField(primary_key=True)
    pracownik = models.ForeignKey('Pracownik', models.SET('usunieto'), db_column='pracownik', related_name='+')
    ilosc = models.FloatField()

    class Meta:
        db_table = 'nadgodziny'


class Pracownik(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.SET('usunieto'), default=None, null=True, blank=True)
    stanowisko = models.ForeignKey('Stanowisko', models.SET('usunieto'), db_column='stanowisko', related_name='+')
    budynek = models.IntegerField(null=True, blank=True)
    imie = models.TextField()
    nazwisko = models.TextField()
    telefon = models.TextField()
    email = models.TextField()
    adres = models.ForeignKey('Adres', models.SET('usunieto'), db_column='adres', related_name='+')

    class Meta:
        db_table = 'pracownik'


class Licznik(models.Model):
    id = models.AutoField(primary_key=True)
    typ = models.TextField()
    cena_netto = models.FloatField()

    class Meta:
        db_table = 'licznik'


class StanLicznik(models.Model):
    id = models.AutoField(primary_key=True)
    typ = models.ForeignKey('Licznik', models.SET('usunieto'), db_column='typ', related_name='+')
    mieszkanie = models.ForeignKey('Mieszkanie', models.SET('usunieto'), db_column='mieszkanie', related_name='+')
    stan = models.FloatField()

    class Meta:
        db_table = 'stan_licznik'


class Stanowisko(models.Model):
    id = models.AutoField(primary_key=True)
    nazwa = models.TextField()
    pensja = models.IntegerField()
    group = models.OneToOneField(Group, on_delete=models.SET('usunieto'), default=None, null=True, blank=True)

    class Meta:
        db_table = 'stanowisko'


class Wlasciciel(models.Model):
    id = models.AutoField(primary_key=True)
    imie = models.TextField()
    nazwisko = models.TextField()
    telefon = models.TextField()
    email = models.TextField()
    mieszkanie = models.ForeignKey('Mieszkanie', models.SET('usunieto'), db_column='mieszkanie', blank=True, null=True, related_name='+')

    class Meta:
        db_table = 'wlasciciel'


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    pracownik = models.TextField(null=True, blank=True)
    zglaszajacy = models.TextField(default=None, null=True, blank=True)
    opis = models.TextField()
    data = models.DateField(default=timezone.now, null=True, blank=True)

    class Meta:
        db_table = 'ticket'


class Wydarzenie(models.Model):
    id = models.AutoField(primary_key=True)
    nazwa = models.TextField()
    opis = models.TextField()
    data = models.DateField()
    budynek = models.ForeignKey('Budynek', models.SET('usunieto'), db_column='budynek', blank=True, null=True, related_name='+')

    class Meta:
        db_table = 'wydarzenie'


class Wystawca(models.Model):
    id = models.AutoField(primary_key=True)
    nazwa = models.TextField()
    kod_pocztowy = models.TextField()
    miasto = models.TextField()
    ulica = models.TextField()
    telefon = models.TextField()
    email = models.TextField()

    class Meta:
        db_table = 'wystawca'
