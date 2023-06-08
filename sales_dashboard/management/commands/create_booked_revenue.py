
from django.core.management.base import BaseCommand
from sales_dashboard.models import BookedRevenue

class Command(BaseCommand):
    help = 'Creates the Zimmer Biomet Booked Revenue Page'

    def handle(self, *args, **options):
        BookedRevenue.objects.get_or_create(
            title='Zimmer Biomet Booked Revenue Outstanding',
            defaults={
                'description': 'ZB Rigid FIxation Implanted PO Outstanding',
                'embed_url': "https://airtable.com/embed/shrcvND1bLfN820kF?backgroundColor=blue&viewControls=on"
            }
        )
