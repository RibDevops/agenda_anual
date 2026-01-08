from django.shortcuts import render, redirect
from datetime import date, datetime
from .models import Evento
from .calendario import gerar_calendario_anual

def home(request):
    return render(request, 'agenda/home.html')

def adicionar_evento(request):
    data_pre_preenchida = request.GET.get('data')
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        data_str = request.POST.get('data')
        cor = request.POST.get('cor')
        if titulo and data_str:
            data_obj = datetime.strptime(data_str, '%Y-%m-%d').date()
            Evento.objects.create(titulo=titulo, data=data_obj, cor=cor)
            return redirect('agenda:agenda_anual')
    return render(request, 'agenda/event.html', {'data_pre_preenchida': data_pre_preenchida})

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
        'eventos_por_data': eventos_por_data,
        'todos_eventos': eventos
    })


# adicione no topo:
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

# função existente agenda_anual permanece
def gerar_pdf(request):
    ano = int(request.GET.get('ano', date.today().year))
    calendario = gerar_calendario_anual(ano)
    eventos = Evento.objects.filter(data__year=ano)
    eventos_por_data = {}
    for e in eventos:
        eventos_por_data.setdefault(e.data, []).append(e)

    html_string = render_to_string('agenda/anual_print.html', {
        'ano': ano,
        'calendario': calendario,
        'eventos_por_data': eventos_por_data
    })

    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    pdf = html.write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="calendario_{ano}.pdf"'
    return response