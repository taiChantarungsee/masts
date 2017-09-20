from django.db import models
from datetime import datetime

class CsvData(models.Model):
	name = models.CharField(max_length=30)
	address1 = models.CharField(max_length=30)
	address2 = models.CharField(max_length=30)
	address3 = models.CharField(max_length=30)
	address4 = models.CharField(max_length=30)
	unit_name = models.CharField(max_length=30)
	tenant_name = models.CharField(max_length=30)
	lease_start_date = models.CharField(max_length=30, null=True)
	lease_end_date = models.CharField(max_length=30, null=True)
	lease_years = models.IntegerField(null=True)
	current_rent = models.FloatField(null=True)

	def get_start_date(self):
		start_date = datetime.strptime(self.lease_start_date, '%d-%m-%Y')
		return start_date