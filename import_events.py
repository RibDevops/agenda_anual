import os
import django
import pandas as pd
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from agenda.models import Evento

def import_events():
    # Use a simpler approach that doesn't rely on complex numpy stuff if possible
    # or just try to fix the import error by ensuring we don't use heavy pandas features
    file_path = 'attached_assets/Calendário_2026_1767840289023.xlsx'
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    try:
        # Try reading with openpyxl directly to avoid some numpy dependencies
        df = pd.read_excel(file_path, engine='openpyxl')
        print(f"Columns: {df.columns.tolist()}")
        
        # Example mapping based on common structures
        # If columns are 'Data', 'Evento', 'Cor'
        for _, row in df.iterrows():
            data_val = row.get('Data')
            titulo = row.get('Evento') or row.get('Titulo')
            cor = row.get('Cor', 'azul')
            
            if pd.notnull(data_val) and pd.notnull(titulo):
                if isinstance(data_val, str):
                    try:
                        data_val = datetime.strptime(data_val, '%Y-%m-%d').date()
                    except:
                        continue
                
                Evento.objects.get_or_create(
                    data=data_val,
                    titulo=titulo,
                    defaults={'cor': cor}
                )
        print("Import finished.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    import_events()
