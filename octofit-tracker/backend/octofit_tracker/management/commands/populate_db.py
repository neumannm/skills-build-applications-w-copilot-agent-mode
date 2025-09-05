from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Lösche alle Daten
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Benutzer
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='test', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='test', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='test', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='test', team=dc),
        ]

        # Aktivitäten
        Activity.objects.create(user=users[0], type='Run', duration=30, distance=5)
        Activity.objects.create(user=users[1], type='Swim', duration=45, distance=2)
        Activity.objects.create(user=users[2], type='Bike', duration=60, distance=20)
        Activity.objects.create(user=users[3], type='Run', duration=50, distance=10)

        # Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        Workout.objects.create(name='Strength Training', description='Strength for super heroes', duration=60)

        # Leaderboard
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[1], points=80)
        Leaderboard.objects.create(user=users[2], points=120)
        Leaderboard.objects.create(user=users[3], points=110)

        self.stdout.write(self.style.SUCCESS('Testdaten erfolgreich in octofit_db eingefügt.'))
