from django.test import TestCase
from main.models import BodyWeight
from main.forms import BodyWeightForm
from users import forms,models
from main.views import BweightView
from django.urls import reverse
from unittest.mock import patch
from django.contrib import auth
from django.test.client import Client

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
        self.client = Client()
        obj = models.CustomUser.objects.create_user(email='frankchuka250@gmail.com',password='testpass123',first_name='Frank',last_name='zico',birth_date='1993-11-11',gender='m')
        
    def test_getformview_status_code(self):
        self.client.login(password='testpass123',email='frankchuka250@gmail.com')
        request = self.client.get(reverse('main:weight'))
        self.assertEquals(request.status_code,200)
        
    def test_postformview_status_code(self):
        request = self.client.post(reverse('main:weight'),{'weight':77})
        self.assertEqual(request.status_code, 302)

    def test_html_template_used(self):
        self.client.login(password='testpass123',email='frankchuka250@gmail.com')
        request = self.client.get(reverse('main:weight'))
        self.assertTemplateUsed(request,'main/chart.html')

    def test_contains_correct_html(self):
        self.client.login(password='testpass123',email='frankchuka250@gmail.com')
        request = self.client.get(reverse('main:weight'))
        self.assertContains(request,'Welcome')
    
    def test_listdata_method(self):
        b=BweightView()
        self.assertEqual(type(b.datalist(BodyWeight)),list)
 
class TestSignupPage(TestCase):
    def test_user_signup_page_load_corrects(self):
        response = self.client.get(reverse('main:signup'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"main/signup.html")
        self.assertContains(response,"Create a new account")
        self.assertIsInstance(response.context['form'],forms.UserCreationForm)

    def test_user_signup_page_submission_works(self):
        post_data = {
            'email':'zico@gmail.com',
            'first_name': 'Frank',
            'last_name':  'zico',
            'birth_date': '1993-11-11',
            'gender': 'm',
            'password1':'testpass123',
            'password2':'testpass123',
        }
        with patch.object(forms.CustomUserCreationForm,"send_mail") as mock_send:
            response = self.client.post(reverse('main:signup'),post_data)
        self.assertEqual(response.status_code,302)
        self.assertTrue(models.CustomUser.objects.filter(email='zico@gmail.com').exists())
        self.assertTrue(auth.get_user(self.client).is_authenticated)
        mock_send.assert_called_once()
    