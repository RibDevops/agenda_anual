import calendar
from datetime import date

def gerar_calendario_anual(ano):
    calendario = {}

    for mes in range(1, 13):
        semanas = calendar.Calendar(calendar.SUNDAY).monthdatescalendar(ano, mes)
        calendario[mes] = semanas

    return calendario
