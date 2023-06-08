# sales_dashboard/management/commands/create_zimmer.py

from django.core.management.base import BaseCommand
from sales_dashboard.models import DashboardView

class Command(BaseCommand):
    help = 'Creates the Zimmer Biomet Sales Dashboard'

    def handle(self, *args, **options):
        DashboardView.objects.get_or_create(
            title='Zimmer Biomet Sales Dashboard',
            defaults={
                'description': 'Monthly Rolling by Account',
                'time_period': '2022 - Present',
                'sheets_url': "https://docs.google.com/spreadsheets/d/e/2PACX-1vRZwivESjq4vguXpiTJSIhTg0ScbGuimZYuxfhAFS4iiqXv13OZ7JKO3g1mMsjJF6QZlA2c8eE23eAr/pubhtml?gid=606071553&amp;single=true&amp;widget=true&amp;headers=false"
            }
        )
