from django.test import TestCase,Client
# Create your tests here.
from .models import CycleSetting
from rest_framework import status
from .serializers import CycleSettingSerializer
from django.urls import reverse
import json
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
import pytest





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
    
    @property
    def bearer_token(self):
        '''
        creates a test user and Get refresh token for authentication
        '''
        user = User.objects.create(username = 'paultrigcode',password ='paultrig')
        client = APIClient()
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION":f'Bearer {refresh.access_token}'}
    
    def test_cycle_settings_average(self):
        cycle_setting = CycleSetting.objects.get(cycle_average=25)
        self.assertEqual(
            cycle_setting.get_cycle_average(), 25)
        self.assertEqual(
            cycle_setting.get_period_average(), 5)

    def test_valid_cycle_create_settings(self):
       response = self.client.post(reverse('cycle_create-list'), data = self.valid_payload, **self.bearer_token)
       self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_cycle_create_settings(self):
        response = self.client.post(reverse('cycle_create-list'), data = self.invalid_payload, **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)



