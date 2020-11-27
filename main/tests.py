from django.test import TestCase
from main.models import BodyWeight
from main.forms import BodyWeightForm
from django.urls import reverse

class TestModel(TestCase):
    def setUp(self):
        self.bweight=BodyWeight.objects.create(
            weight=77
        )
    def test_weight_contains_correct_values(self):
        self.assertEquals(self.bweight.weight,77)
    
    def test_weight_doesNotContain_correct_value(self):
        self.assertNotEqual(self.bweight.weight,79)

class TestForm(TestCase):
    def setUp(self):
        data = {'weight':150}
        self.form = BodyWeightForm(data)
        
    def test_form_isvalid(self):
        self.assertTrue(self.form.is_valid())
    
    def test_form_isinvalid(self):
        data = {'weight':'twenty'}
        self.form = BodyWeightForm(data)
        self.assertFalse(self.form.is_valid())


class TestView(TestCase):
    def setUp(self):
        self.get_request = self.client.get(reverse('bwv'))
        self.post_request = self.client.post(reverse('bwv'),{'weight':77})
    def test_getformview_status_code(self):
        self.assertEquals(self.get_request.status_code,200)
        
    def test_postformview_status_code(self):
        self.assertEqual(self.post_request.status_code, 302)
