from django.test import TestCase
from django.core.management import call_command
from django.test.client import Client
from .models import CsvData
from .forms import MastForm

class Mast_app_Test(TestCase):
	"""Testing that we get the correct data back from templates"""

	fixtures = ["mast_app.json"]

	def test_index(self):
		c = Client()
		res = c.get("/masts/")
		self.assertEquals(res.status_code, 200)
		self.assertTrue(b"This table presents" in res.content)

class Model_Tests(TestCase):
	""" A series of model tests querying and saving data"""

	fixtures = ["mast_app.json"]

	def test_query(self):
		test = CsvData.objects.get(name="Beecroft Hill")
		self.assertEquals(test.tenant_name, "Arqiva Services ltd")

	def test_save(self):
		test = CsvData.objects.create(
				name="Test",
				address1 = "Test",
				address2 = "Test",
				address3 = "Test",
				address4 = "Test",
				unit_name = "Test",
				tenant_name = "Test",
				lease_start_date = "02-03-1999",
				lease_end_date = "04-03-2017",
				lease_years = 4,
				current_rent = 5,)
		test = CsvData.objects.get(name="Test")
		self.assertEquals(test.tenant_name, "Test")

class Form_Tests(TestCase):
	""" Test the form separately from everything else"""

	def test_form(self):
		Form = MastForm()

		# Check some fields are there, as_p() renders in html
		self.assertIn("tenant_name", Form.as_p())
		self.assertIn("address1", Form.as_p())

		Form = MastForm(data= {"name": "test_name",
							   "address1": "test",
							   "address2": "test",
							   "address3": "test",
							   "address4": "test",
							   "unit_name": "test",
							   "tenant_name": "test",
							   "lease_start_date": "02-03-1999",
							   "lease_end_date": "04-03-2017",
							   "lease_years": 43,
							   "current_rent": 44
								})

		self.assertTrue(Form.is_valid())
		self.assertIn("name", Form.as_p()) 

		# Now save the data, which will clean it, and test it
		saved = Form.save()

		self.assertEqual(saved.name, "test_name")
		self.assertEqual(saved.current_rent, 44)

		#Now change the data in a field to an invalid data type, and check the error message
		Form = MastForm(data= {"name": 1})

		# is_valid should return false if there are errors
		self.assertFalse(Form.is_valid())

		# Since address1 and address2 are required fields they should return an error
		self.assertTrue("address1" in Form.errors.keys())
		self.assertTrue("address2" in Form.errors.keys())
		self.assertEqual(Form.errors["address1"], ["This field is required."])
		self.assertEqual(Form.errors["address2"], ["This field is required."])