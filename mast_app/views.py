from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import CsvData
from .forms import MastForm
from datetime import datetime
from django.core import serializers

#Function to convert dates into the right format.
#def monthToNum(tenant):
#	tenant.lease_start_date = datetime.strptime(tenant.lease_start_date, '%d-%b-%y').strftime('%d-%m-%Y')
#	tenant.lease_end_date =  datetime.strptime(tenant.lease_end_date, '%d-%b-%y').strftime('%d-%m-%Y')
#	tenant.save()

def index(request):
	#Handle forms first.
	if request.method == "POST":
		form = MastForm(request.POST)
		if form.is_valid():
			print("is valid")
			mast = form.save()
			return redirect('/masts/')
	else:
		form = MastForm()

	#Produce a list sorted by lease amount (rent) in ascending order.
	rent_ascending = CsvData.objects.order_by('current_rent')[:5]

	#For displaying the total rent for all items in the list.
	total_rent = CsvData.objects.aggregate(Sum('current_rent'))
	total_rent_value = total_rent.get('current_rent__sum')
	#Create a dictionary containing tenant names and a count of masts, to display as a list.
	tenants = CsvData.objects.all()
	dictionary = {}
	for tenant in tenants:
		number_of_masts = 0
		for other_tenants in tenants:
			if other_tenants.tenant_name == tenant.tenant_name:
				number_of_masts += 1
		dictionary[tenant.tenant_name] = number_of_masts
		
	#List the data for rentals with lease dates from 1 june 1999 and 31 August 2007 with format of DD/MM/YYYY.
	#Convert fields first.
	rental_dates = []
	for tenant in tenants:
		start_date = datetime.strptime(tenant.lease_start_date, '%d-%m-%Y')
		start = datetime.strptime('01-06-1999', '%d-%m-%Y')
		end = datetime.strptime('31-08-2007', '%d-%m-%Y')
		if start_date > start and start_date < end:	
			rental_dates.append(tenant)

	#For formatting dates in models correctly
	#for tenant in tenants:
	#	monthToNum(tenant)

	#Send all the processed data to the context.
	context = {
		'form':form,
		'rent_ascending':rent_ascending,
		'total_rent_value':total_rent_value,
		'rental_dates':rental_dates,
		'dictionary':dictionary,
		#'rental_dates':rental_dates,
	}
	return render(request, 'masts/index.html', context)