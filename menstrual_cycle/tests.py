from django.test import TestCase
# Create your tests here.
from .models import CycleSetting


class CycleSettingTest(TestCase):
    """ Test module for CycleSetting model """

    def setUp(self):
        CycleSetting.objects.create(
            last_period_date='2020-06-20', cycle_average = 25, period_average = 5, start_date='2020-07-25',end_date ='2021-07-25' )
        # CycleSetting.objects.create(
        #     last_period_date='2020-06-20', cycle_average = 25, period_average ='Bull Dog', start_date='2020-07-25',end_date ='2021-07-25' )

    def test_puppy_breed(self):
        cycle_setting = CycleSetting.objects.get(cycle_average=25)
        self.assertEqual(
            cycle_setting.get_cycle_average(), 25)
        self.assertEqual(
            cycle_setting.get_period_average(), 5)