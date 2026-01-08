from . import views
from django.urls import path

app_name = 'agenda'

urlpatterns = [
    path('', views.home, name='home'),
    path('agenda/', views.agenda_anual, name='agenda_anual'),
    path('evento/novo/', views.adicionar_evento, name='adicionar_evento'),
    path('gerar-pdf/', views.gerar_pdf, name='gerar_pdf'),
]
