from django.db import models


class Pasazerowie(models.Model):
    pesel = models.CharField(max_length=11)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)


class Rezerwacje(models.Model):
    pasazer = models.ForeignKey(Pasazerowie, on_delete=models.CASCADE)
    data = models.DateTimeField()


class Lotniska(models.Model):
    nazwa = models.CharField(max_length=20)


class Trasy(models.Model):
    miejsce_odlotu = models.ForeignKey(Lotniska, related_name="miejsce_odlotu", on_delete=models.CASCADE)
    miejsce_przylotu = models.ForeignKey(Lotniska, related_name="miejsce_przylotu", on_delete=models.CASCADE)


class Samoloty(models.Model):
    ilosc_miejsc = models.IntegerField()


class Loty(models.Model):
    data_odlotu = models.DateTimeField()
    data_przylotu = models.DateTimeField()
    trasa = models.ForeignKey(Trasy, on_delete=models.CASCADE)
    samolot = models.ForeignKey(Samoloty, on_delete=models.CASCADE)
    numer_lotu = models.CharField(max_length=10)


class Siedzenia(models.Model):
    samolot = models.ForeignKey(Samoloty, on_delete=models.CASCADE)
    lot = models.ForeignKey(Loty, on_delete=models.CASCADE)
    pasazer = models.ForeignKey(Pasazerowie, on_delete=models.CASCADE)
    miejsce = models.IntegerField()


class Wymagania(models.Model):
    nazwa = models.CharField(max_length=30)


class MiejscaSpecjalne(models.Model):
    wymaganie = models.ForeignKey(Wymagania, on_delete=models.CASCADE)
    siedzenie = models.ForeignKey(Siedzenia, on_delete=models.CASCADE)
