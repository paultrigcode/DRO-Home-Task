from django.test import TestCase,Client
# Create your tests here.
from .models import CycleSetting
from rest_framework import status
from .serializers import CycleSettingSerializer
from django.urls import reverse
import json
from rest_framework.test import APIClient





class CycleSettingTest(TestCase):
    """ Test module for CycleSetting model """

    def setUp(self):
        CycleSetting.objects.create(
            last_period_date='2020-06-20', cycle_average = 25, period_average = 5, start_date='2020-07-25',end_date ='2021-07-25' )
        # CycleSetting.objects.create(
        #     last_period_date='2020-06-20', cycle_average = 25, period_average ='Bull Dog', start_date='2020-07-25',end_date ='2021-07-25' )
        self.valid_payload = {
            'last_period_date': '2020-06-20',
            'cycle_average': 25,
            'period_average': 5,
            'start_date': '2020-07-25',
            'end_date':'2021-07-25'
        }
        self.invalid_payload = {
            'last_period_date': '',
            'cycle_average': 25,
            'period_average': 5,
            'start_date': '2020-07-25',
            'end_date':'2021-07-25'
        }
        self.user_credentials = {
            'username': 'paultrigcode',
            'password': 'paultrig',
        }
    
    def test_cycle_settings_average(self):
        cycle_setting = CycleSetting.objects.get(cycle_average=25)
        self.assertEqual(
            cycle_setting.get_cycle_average(), 25)
        self.assertEqual(
            cycle_setting.get_period_average(), 5)

    # def test_create_cycle_setting(self):
    #     client = Client()
    #     header = {'Authorization':'Bearer '}
    #     response1 = client.post(
    #     			reverse('token_refresh'),
    #     			data = json.dumps(self.user_credentials),
    # 				content_type = 'application/json',
    # 				)
    #     print(response1.json())
    #     response = client.post(
    #         reverse('cycle_create-list'),
    #         data=json.dumps(self.valid_payload),
    #         content_type='application/json',
    #         header = header
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_cycle_setting(self):
        client = APIClient()
        client.login(username='paultrigcode', password='paultrig')
        response = client.post('/cycle_create/', {
            'last_period_date': '2020-06-20',
            'cycle_average': 25,
            'period_average': 5,
            'start_date': '2020-07-25',
            'end_date':'2021-07-25'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

