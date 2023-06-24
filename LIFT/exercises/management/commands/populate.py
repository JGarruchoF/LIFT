# IMPORTS PYTHON
import csv
from tqdm import tqdm

# IMPORTS DJANGO
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError

# IMPORTS SELF
from exercises.models import Muscle, Equipment, Exercise

# BODY_PART = 0
EQUIPMENT = 1
GIFT_URL = 2
# ID = 3
EXERCISE_NAME = 4
TARGET = 5



class Command(BaseCommand):
    help = "Populate exercises models from .csv file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help='Path to .csv file')
        parser.add_argument('--clean', action='store_true', help='Clean database before populating')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        clean = options['clean']

        if clean:
            Muscle.objects.all().delete()
            Equipment.objects.all().delete()
            Exercise.objects.all().delete()

        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            next(reader)
            rows = list(reader)
            total = len(rows)

            for _, row in enumerate(tqdm(rows, total=total)):
                try:
                    muscle, _ = Muscle.objects.get_or_create(name=row[TARGET])
                except Exception as e:
                    print(e)

                try:
                    equipment, _ = Equipment.objects.get_or_create(name=row[EQUIPMENT])
                except Exception as e:
                    print(e)


                exercise = Exercise(name=row[EXERCISE_NAME], target=muscle, equipment=equipment, gif_url=row[GIFT_URL])
                try:
                    exercise.save()
                except Exception as e:
                    print(row[EXERCISE_NAME])
                    print(e)
