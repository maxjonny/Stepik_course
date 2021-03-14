from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404

directions = {
    "from_Moscow": 'Москвы',
    "from_St.Petersburg": 'Петербурга',
    "from_Novosibirsk": 'Новосибирска',
    "from_Ekaterinburg": 'Екатеринбурга',
    "from_Kazan": 'Казани'
}

tour_number = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6
}


def main_view(request):
    return render(request, 'index.html')


def departure_view(request, departure):
    try:
        city = directions[departure]
    except KeyError:
        raise Http404
    return render(request, 'departure.html', context={'city': city})


def tour_view(request, id):
    try:
        tour_number[id]
    except KeyError:
        raise Http404
    return render(request, 'tour.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... <br> Простите извините!')
