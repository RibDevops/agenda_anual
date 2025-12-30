from . import views
from django.urls import path

app_name = 'agenda'

urlpatterns = [
    # path('', views.home, name='home'),
    path('agenda/', views.agenda_anual, name='agenda_anual'),
]
