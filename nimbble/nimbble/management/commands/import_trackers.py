from django.core.management.base import BaseCommand, CommandError
from nimbble.dbconfig.trackers import CustomFitnessTrackerMigration


class Command(BaseCommand):
    help = 'Import the default fitness tracker information.'

    def handle(self, *args, **options):
        mig = CustomFitnessTrackerMigration()
        mig.import_tracker_info()
