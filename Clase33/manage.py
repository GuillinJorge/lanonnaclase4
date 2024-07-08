#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_api_peliculas.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


curl -X POST http://127.0.0.1:8000/pelicula/ \
    -H "Content-Type: application/json" \
    -d '{
        "nomnbre": "Rocky IV",
        "duracion": 120,
        "fecha_de_release": "1998-05-03",
        "genero": "Deportes"
    }'