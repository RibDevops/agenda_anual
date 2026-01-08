from . import views
from django.urls import path

app_name = 'agenda'

urlpatterns = [
    path('', views.agenda_anual, name='agenda_anual'),
    path('gerar-pdf/', views.gerar_pdf, name='gerar_pdf'),
]
