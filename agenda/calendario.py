import calendar
from datetime import date

def gerar_calendario_anual(ano):
    calendario_data = {}
    nomes_meses = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]

    for mes_idx, mes_nome in enumerate(nomes_meses, 1):
        # Transpor semanas para que tenhamos dias da semana nas linhas e semanas nas colunas
        semanas = calendar.Calendar(calendar.SUNDAY).monthdatescalendar(ano, mes_idx)
        # semanas é uma lista de listas (semana 1, semana 2, etc.)
        # queremos [dom_s1, dom_s2, ...], [seg_s1, seg_s2, ...], etc.
        linhas_dias = [[] for _ in range(7)]
        for semana in semanas:
            for dia_idx, dia in enumerate(semana):
                linhas_dias[dia_idx].append(dia)
        
        calendario_data[mes_nome] = linhas_dias

    return calendario_data
