from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@csrf_exempt
def pasazer(request):
    if request.method == 'GET':
        template = "pasazer.html"
        loty = Loty.objects.all()
        context = {'loty': loty}
        return render(request, template, context)
    elif request.method == "POST":
        template = 'siedzenia.html'
        imie = request.POST.get('imie')
        nazwisko = request.POST.get('nazwisko')
        pesel = request.POST.get('pesel')
        pasazerowie = Pasazerowie.objects.all()
        for x in pasazerowie:
            if pesel == x.pesel:
                if nazwisko == x.nazwisko:
                    if imie == x.imie:
                        existing_id = x.id
                        url = '/siedzenia/' + str(x.id)
                        return redirect(url)
                    else:
                        loty = Loty.objects.all()
                        error = 'Podany pesel istnieje juz w bazie!'
                        context = {'loty': loty, 'error': error}
                        template = "pasazer.html"
                        return render(request, template, context)
                else:
                    loty = Loty.objects.all()
                    error = 'Podany pesel istnieje juz w bazie!'
                    context = {'loty': loty, 'error': error}
                    template = "pasazer.html"
                    return render(request, template, context)
        pasazerek = Pasazerowie(imie=imie, nazwisko=nazwisko, pesel=pesel)
        pasazerek.save()
        pasazer_id = pasazerek.id
        url = '/siedzenia/' + str(pasazer_id)
        return redirect(url)


def siedzenia(request, pasazer_id):
    if request.method == 'GET':
        template = "siedzenia.html"
        aktualny_pasazer = Pasazerowie.objects.get(pk=pasazer_id)
        context = {'aktualny_pasazer': aktualny_pasazer, 'pasazer_id': pasazer_id}
        return render(request, template, context)
    if request.method == 'POST':
        url = '/siedzenia/' + str(pasazer_id)
        return redirect(url)


def rezerwacje(request):
    return render(request, template, context)
