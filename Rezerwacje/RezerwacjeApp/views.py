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

        pasazerek = Pasazerowie(imie=imie, nazwisko=nazwisko, pesel=pesel)
        pasazerek.save()
        pasazer_id = pasazerek.id
        url = '/siedzenia/' + str(pasazer_id)
        return redirect(url)


def siedzenia(request, pasazer_id):
    template = "siedzenia.html"
    return render(request, template)
