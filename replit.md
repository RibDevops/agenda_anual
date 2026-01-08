# Agenda Anual

## Overview

This is a Django-based annual calendar/agenda application designed to display and manage events throughout the year. The system renders a 12-month calendar view with events displayed on their respective dates, supports PDF export functionality, and allows importing events from Excel spreadsheets.

The application is built for organizing schedules (escalas) and shift planning (plantões), displaying events color-coded by type on a responsive calendar grid.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Framework
- **Django 4.2+**: Standard Django MVC architecture with the project split into:
  - `core/`: Main Django project configuration (settings, URLs, WSGI/ASGI)
  - `agenda/`: Primary application containing models, views, and calendar logic

### Database Design
- **SQLite** (Django default): Two main models:
  - `TipoEvento`: Event type categorization with a `tipo` field
  - `Evento`: Individual events with foreign key to `TipoEvento`, plus `titulo`, `data` (date), and `cor` (color) fields

### Calendar Generation
- Custom calendar utility (`agenda/calendario.py`) uses Python's built-in `calendar` module
- Generates week-by-week date grids for each month, starting weeks on Sunday
- Events are grouped by date and passed to templates as a dictionary lookup

### Template Architecture
- Uses Django template language with custom template tags (`agenda_filters.py`)
- `get_item` filter enables dictionary lookups in templates
- Templates located in `templates/agenda/` directory
- Separate templates for web view (`anual.html`) and PDF generation (`anual_print.html`)

### PDF Generation
- **WeasyPrint**: Converts HTML templates to PDF documents
- Renders the same calendar data to a print-specific template
- Returns PDF as downloadable attachment

### Data Import
- Standalone script (`import_events.py`) for importing events from Excel files
- Uses pandas with openpyxl engine for Excel parsing
- Expects columns: Data, Evento/Titulo, Cor

### URL Structure
- `/`: Annual calendar view (accepts `?ano=YYYY` parameter)
- `/gerar-pdf/`: PDF export endpoint
- `/admin/`: Django admin interface

## External Dependencies

### Python Packages
- **Django 4.2+**: Web framework
- **pandas**: Data manipulation for Excel import
- **openpyxl**: Excel file reading engine
- **WeasyPrint**: HTML to PDF conversion (requires system-level dependencies for Cairo/Pango)

### Static Assets
- Custom CSS (`static/agenda.css`) for calendar grid styling
- Responsive grid layout using CSS Grid with auto-fit columns

### Configuration Notes
- Debug mode enabled with `ALLOWED_HOSTS = ['*']`
- CSRF trusted origins configured for Replit domains
- Uses Django's default SQLite database
- Static files served through Django's staticfiles app