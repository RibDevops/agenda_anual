from django.core.management.base import BaseCommand
import pandas as pd
from datetime import datetime
from agenda.models import Evento, TipoEvento

class Command(BaseCommand):
    help = "Importa eventos do CSV modelo"

    def add_arguments(self, parser):
        parser.add_argument('arquivo', type=str, help='Caminho para o CSV')

    def handle(self, *args, **options):
        arquivo = options['arquivo']
        df = pd.read_csv(arquivo, header=None, dtype=str, encoding='utf-8', keep_default_na=False)
        # Procura por padrões de data no formato DD/MM - Título
        import re
        date_re = re.compile(r'(\d{2}/\d{2})\s*-\s*(.+)')
        for _, row in df.iterrows():
            for cell in row:
                if not isinstance(cell, str):
                    continue
                m = date_re.search(cell)
                if m:
                    date_str = m.group(1) + '/2025'  # ano fixo 2025; torne configurável se precisar
                    titulo = m.group(2).strip()
                    try:
                        data = datetime.strptime(date_str, '%d/%m/%Y').date()
                    except Exception:
                        continue
                    tipo, _ = TipoEvento.objects.get_or_create(tipo='feriado')
                    Evento.objects.get_or_create(
                        titulo=titulo,
                        data=data,
                        tipo_id=tipo,
                        defaults={'cor': 'red'}
                    )
        self.stdout.write(self.style.SUCCESS('Import concluído'))
