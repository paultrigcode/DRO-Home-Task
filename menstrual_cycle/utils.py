from datetime import datetime, date, time, timedelta
import pytest
def calculate_number_of_cycles(last_period_date_obj,start_date_time_obj,end_date_time_obj):  
	date_dict = {}
	while last_period_date_obj < end_date_time_obj:
		period_start_date = last_period_date_obj+timedelta(25)
		if period_start_date > end_date_time_obj:
			break
		period_end_date = period_start_date+timedelta(5)
		print(period_start_date,period_end_date)
		if not period_start_date < start_date_time_obj :
	 		date_dict[period_start_date] = period_end_date
		last_period_date_obj = period_end_date

	return date_dict
