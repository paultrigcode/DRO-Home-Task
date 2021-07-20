from django.db import models

# Create your models here.

class CycleSetting(models.Model):
	last_period_date = models.DateField()
	cycle_average = models.IntegerField(default = 0)
	period_average = models.IntegerField(default = 0)
	start_date = models.DateField()
	end_date = models.DateField()