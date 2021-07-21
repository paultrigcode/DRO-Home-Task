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
        '''
        Asserts that it returns the cycle average and period average values correctly
        '''
        cycle_setting = CycleSetting.objects.get(cycle_average=25)
        self.assertEqual(
            cycle_setting.get_cycle_average(), 25)
        self.assertEqual(
            cycle_setting.get_period_average(), 5)

    def test_valid_cycle_create_settings(self):
       '''
       Asserts that it returns 200 status code when any of the field is empty or missing
       '''
       response = self.client.post(reverse('cycle_create-list'), data = self.valid_payload, **self.bearer_token)
       self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_cycle_create_settings(self):
        '''
        Asserts that it returns 422 error status code when any of the field is empty or missing
        '''
        response = self.client.post(reverse('cycle_create-list'), data = self.invalid_payload, **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_cycle_event_request(self):
        '''
        Asserts that it returns 200 Ok status code when the cycle_event endpoint is queried with a valid date param
        '''
        response = self.client.get(reverse('cycle_event-list'), {'date':'2020-08-04'}, **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


