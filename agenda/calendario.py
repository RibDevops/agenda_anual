import calendar
from datetime import date

def gerar_calendario_anual(ano):
    calendario_data = {}
    nomes_meses = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]

    for mes in range(1, 13):
        semanas = calendar.Calendar(calendar.SUNDAY).monthdatescalendar(ano, mes)
        # Usar o nome do mês como chave para facilitar no template
        calendario_data[nomes_meses[mes-1]] = semanas

    return calendario_data
