from django.shortcuts import render
from rest_framework.response import Response
from .import serializers
from .models import CycleSetting
from rest_framework import generics, permissions, status, viewsets
from cerberus import Validator
from datetime import datetime, date, time, timedelta
import math
from .utils import calculate_number_of_cycles


# Create your views here.
class CycleSettingViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.CycleSettingSerializer
    queryset = CycleSetting.objects.all()
    schema = {
        'last_period_date': {'type': 'string','empty': False},
        'cycle_average':{'type':'string','empty': False},
        'period_average':{'type':'string','empty': False},
        'start_date': {'type' : 'string','empty': False},
        'end_date': {'type' : 'string','empty': False}
    }

    
    def get_queryset(self):
        return super().get_queryset().filter()

    def create(self,request):
        v = Validator(self.schema)
        v.require_all = True
        if not v.validate(request.data):
            return Response({
                "errors": v.errors
            }, status.HTTP_422_UNPROCESSABLE_ENTITY)

        if CycleSetting.objects.all():
            return Response({'message':'cycle setting already exist, You can only update cycle setting after creating one, please kindly update existing cycle settings from django admin'})
        delta = timedelta(days=30)
        start_date = request.data['start_date']
        end_date = request.data['end_date']
        last_period_date = request.data['last_period_date']
        start_date_time_obj = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_time_obj = datetime.strptime(end_date, '%Y-%m-%d')
        last_period_date_obj = datetime.strptime(last_period_date, '%Y-%m-%d')
        cycle_dict = calculate_number_of_cycles(last_period_date_obj,start_date_time_obj,end_date_time_obj)
        cycle_setting_create = CycleSetting.objects.create(last_period_date = last_period_date,cycle_average = request.data['cycle_average'],
                               period_average = request.data['period_average'],start_date = start_date,end_date = end_date)

        return Response({"total_created_cycles": len(cycle_dict)})

    
class CycleEventViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.CycleSettingSerializer
    queryset = CycleSetting.objects.all()
    def list(self,request):
        date = request.GET.get('date') 
        try:
            date_obj =  datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            return Response({'messgae':'date is invalid'},status.HTTP_400_BAD_REQUEST)
        data =[]
        event_name = [] 
        cycle_setting = list(CycleSetting.objects.all().values())
        start_date_time_obj = cycle_setting[0]['start_date']
        end_date_time_obj = cycle_setting[0]['end_date']
        last_period_date_obj = cycle_setting[0]['last_period_date'] 
        if start_date_time_obj <= date_obj <=  end_date_time_obj:
            while last_period_date_obj < end_date_time_obj:
                period_start_date = last_period_date_obj+timedelta(25)
                if period_start_date > end_date_time_obj:
                   break
                period_end_date = period_start_date+timedelta(5)
                after_period_end =  period_end_date+timedelta(25)
                ovulation_date = period_start_date + timedelta(math.floor(25/2))
                fertility_window1 = ovulation_date -timedelta(4)
                fertility_window2 = ovulation_date+timedelta(4)
                next_period_start_date = period_end_date+timedelta(25)
                print(period_start_date,period_end_date,ovulation_date)
                if fertility_window1 <= date_obj <= fertility_window2 and date_obj != ovulation_date:
                    event = "fertility_window"
                    event_name.append(event)
                elif date == str(period_start_date):
                    event = "Period_start_date"
                    event_name.append(event)
                elif date == str(period_end_date):
                    event = "Period_end_date"
                    event_name.append(event)
                elif date == str(ovulation_date):
                    event = "Ovulation_date"
                    event_name.append(event)
                elif period_end_date < date_obj < fertility_window1 and not period_end_date < date_obj < after_period_end:
                    event = "Pre_ovulationn_window"
                    event_name.append(event)
                elif fertility_window2 < date_obj < next_period_start_date:
                    event = "Post_ovulation_window"
                    event_name.append(event)
                elif period_end_date < date_obj < after_period_end and date_obj != ovulation_date:
                    event = "Pre_ovulation_window"
                    event_name.append(event)

                date_dict = {}
                date_dict['period_start_date'] = period_start_date
                date_dict['period_end_date'] = period_end_date
                date_dict['ovulation_date'] = ovulation_date
                date_dict['fertility_window1'] = fertility_window1
                date_dict['fertility_window2'] = fertility_window2
                data.append(date_dict)

                last_period_date_obj = period_end_date
            data = ''.join(event_name)
            return Response({'date':date,"event": data})	
        else:
            return Response({'message':'date is not in the cycle range in cycle settings,date must be between start and end date specified in cycle setting'},status.HTTP_400_BAD_REQUEST)

