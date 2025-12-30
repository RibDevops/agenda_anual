from django.urls import path
from . import views

app_name = 'agenda'
urlpatterns = [
    path('anual/', views.agenda_anual, name='anual'),
    path('gerar-pdf/', views.gerar_pdf, name='gerar_pdf'),
    # path para upload/import se criar uma view web
]
