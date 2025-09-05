from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username='testuser2', email='test2@example.com', password='testpass')
        activity = Activity.objects.create(user=user, type='Run', duration=30, distance=5.0)
        self.assertEqual(activity.type, 'Run')
        self.assertEqual(activity.duration, 30)
        self.assertEqual(activity.distance, 5.0)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Cardio', description='Cardio session', duration=45)
        self.assertEqual(workout.name, 'Cardio')
        self.assertEqual(workout.duration, 45)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create_user(username='testuser3', email='test3@example.com', password='testpass')
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)

class APIRootTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('workouts', response.data)
        self.assertIn('leaderboard', response.data)
