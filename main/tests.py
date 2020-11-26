from django.test import TestCase
from main.models import BodyWeight

class TestModel(TestCase):
    def setUp(self):
        self.bweight=BodyWeight.objects.create(
            weight=77
        )
    def test_weight_contains_correct_values(self):
        self.assertEquals(self.bweight.weight,77)
    
    def test_weight_doesNotContain_correct_value(self):
        self.assertNotEqual(self.bweight.weight,79)
