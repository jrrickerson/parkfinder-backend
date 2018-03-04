import requests

from django.core.management.base import BaseCommand, CommandError
from parkfinder.parks.mapping import PARK_MAP
from parkfinder.parks.models import Park


class Command(BaseCommand):
    help = 'Import Parks data'

    def add_arguments(self, parser):
        parser.add_argument('url')

    def save_park(self, obj):
        park, _ = Park.objects.get_or_create(global_id=obj['GLOBALID'])
        print('Importing Park {}'.format(obj['GLOBALID']))
        for fieldname in PARK_MAP:
            attr, parse_func = PARK_MAP[fieldname]
            setattr(park, attr, parse_func(obj.get(fieldname)))
        park.save()

    def handle(self, *args, **options):
        resp = requests.get(options['url'])
        json = resp.json()

        for obj in json['parks']:
            try:
                self.save_park(obj)
            except:
                print('Failed to save park {}'.format(str(obj)))
