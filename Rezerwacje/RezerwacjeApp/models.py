from django.db import models


class Pasazerowie(models.Model):
    pesel = models.CharField(max_length=11)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)

    def __str__(self):
        return self.imie + self.nazwisko

class Rezerwacje(models.Model):
    pasazer = models.ForeignKey(Pasazerowie, on_delete=models.CASCADE)
    data = models.DateTimeField()

    def __str__(self):
        return str(self.id) + "- " + str(self.pasazer) + " data rezerwacji: " + str(self.data)[:19]

class Lotniska(models.Model):
    nazwa = models.CharField(max_length=20)

    def __str__(self):
        return self.nazwa

class Trasy(models.Model):
    miejsce_odlotu = models.ForeignKey(Lotniska, related_name="miejsce_odlotu", on_delete=models.CASCADE)
    miejsce_przylotu = models.ForeignKey(Lotniska, related_name="miejsce_przylotu", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.miejsce_odlotu) + " --> " + str(self.miejsce_przylotu)

class Samoloty(models.Model):
    ilosc_miejsc = models.IntegerField()

    def __str__(self):
        return "id=" + str(self.id)

class Loty(models.Model):
    data_odlotu = models.DateTimeField()
    data_przylotu = models.DateTimeField()
    trasa = models.ForeignKey(Trasy, on_delete=models.CASCADE)
    samolot = models.ForeignKey(Samoloty, on_delete=models.CASCADE)
    numer_lotu = models.CharField(max_length=10)

    def __str__(self):
        return self.numer_lotu + " " + str(self.trasa) + " " + str(self.data_odlotu)[:19]


class Siedzenia(models.Model):
    samolot = models.ForeignKey(Samoloty, on_delete=models.CASCADE)
    lot = models.ForeignKey(Loty, on_delete=models.CASCADE)
    pasazer = models.ForeignKey(Pasazerowie, on_delete=models.CASCADE)
    miejsce = models.IntegerField()

    def __str__(self):
        return self.numer_lotu + " " + str(self.miejsce)


class Wymagania(models.Model):
    nazwa = models.CharField(max_length=30)

    def __str__(self):
        return self.nazwa


class MiejscaSpecjalne(models.Model):
    wymaganie = models.ForeignKey(Wymagania, on_delete=models.CASCADE)
    siedzenie = models.ForeignKey(Siedzenia, on_delete=models.CASCADE)

    def __str__(self):
        return self.siedzenie + self.wymaganie
