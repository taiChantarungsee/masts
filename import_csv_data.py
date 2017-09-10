#Script to import all the CSV data into a django model
import csv
from mast_app.models import CsvData

with open('Mobile Phone Masts.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		if row[0] != 'Property Name':
			_, created = CsvData.objects.get_or_create(
				name=row[0],
				address1 = row[1],
				address2 = row[2],
				address3 = row[3],
				address4 = row[4],
				unit_name = row[5],
				tenant_name = row[6],
				lease_start_date = row[7],
				lease_end_date = row[8],
				lease_years = row[9],
				current_rent = row[10],)

print("Script finished!")