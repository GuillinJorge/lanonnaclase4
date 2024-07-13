#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

This script sets the default Django settings module for the 'peliculas_api_django'
project and executes administrative tasks using Django's command-line interface.

Functions:
    main(): Sets the default settings module and executes command-line tasks.

Usage:
    Run this script from the command line to execute administrative tasks such as
    running the development server, migrating the database, or creating a new app.

Example:
    $ python manage.py runserver

Environment Variables:
    DJANGO_SETTINGS_MODULE: Specifies the settings module to be used for the project.
"""

import os
import sys


def main():
    """
    Run administrative tasks.
    
    Sets the default settings module for the Django project to 'peliculas_api_django.settings'
    and executes command-line tasks using Django's management utility.
    
    Raises:
        ImportError: If Django is not installed or cannot be imported.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'peliculas_api_django.settings')
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
