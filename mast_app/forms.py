from django import forms
from .models import CsvData

class MastForm(forms.ModelForm):

	class Meta:

		model = CsvData
		fields = ('name', 'address1', 'address2', 'address3', 'address4', 'unit_name', 'tenant_name', 'lease_start_date',
			'lease_end_date', 'lease_years', 'current_rent')