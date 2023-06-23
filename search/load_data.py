import csv
from django.core.management.base import BaseCommand
from search.models import Restaurant


class Command(BaseCommand):
    help = 'Loads data from restaurants_small.csv into the database.'

    def handle(self, *args, **options):
        with open('restaurants_small.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                name, location, items, lat_long, full_details = row
                Restaurant.objects.create(
                    name=name,
                    location=location,
                    items=items,
                    lat_long = lat_long,
                    full_details=full_details
                )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
