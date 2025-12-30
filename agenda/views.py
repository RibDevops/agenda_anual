from django.shortcuts import render
from datetime import date
from .models import Evento

from .calendario import gerar_calendario_anual
def agenda_anual(request):
    ano = int(request.GET.get('ano', date.today().year))

    calendario = gerar_calendario_anual(ano)
    eventos = Evento.objects.filter(data__year=ano)

    eventos_por_data = {}
    for e in eventos:
        eventos_por_data.setdefault(e.data, []).append(e)

    return render(request, 'agenda/anual.html', {
        'ano': ano,
        'calendario': calendario,
        'eventos_por_data': eventos_por_data
    })
