from django.test import TestCase
from .models import Trip

class TripModelTest(TestCase):
    def setUp(self):
        Trip.objects.create(title="Test Trip", budget=1000.00, code="TEST2023")

    def test_trip_content(self):
        trip = Trip.objects.get(id=1)
        expected_object_name = f'{trip.title}'
        self.assertEqual(expected_object_name, 'Test Trip')