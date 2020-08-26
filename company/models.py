from django.db import models

# Create your models here.
class Company(models.Model):
	company_owner = models.CharField(max_length=30)
	company_name = models.CharField(max_length=30)
	business_type = models.CharField(max_length=30)
	contact_number = models.CharField(max_length=30)
	email = models.EmailField()
	address = models.CharField(max_length=200)
	no_of_sites = models.IntegerField(default=0)

	def __str__(self):
		return self.company_name


class Site(models.Model):

	rd_status_choices = [
		('K-Form', 'K-Form'),
		('Non K-Form', 'Non K-Form'),
		('K-Form Cancellation in progress', 'K-Form Cancellation in progress'),
		('K-Form Canceled', 'K-Form Canceled'),
		('Others', 'Others'),
	]

	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	# General Info
	rd_number = models.IntegerField()
	site_name = models.CharField(max_length=30)
	rd_status = models.CharField(max_length=40, choices=rd_status_choices, default='K-Form')
	supply_point = models.CharField(max_length=30, null=True)
	# Contact
	dealer_name = models.CharField(max_length=30)
	dealer_contact = models.CharField(max_length=30)
	site_address = models.CharField(max_length=200)
	district = models.CharField(max_length=30)
	tehsil = models.CharField(max_length=30)
	# Coordinates
	latitude = models.FloatField()
	longitude = models.FloatField()
	# Area
	zone = models.CharField(max_length=30)
	region = models.CharField(max_length=30)
	zone_manager = models.CharField(max_length=30)
	region_manager = models.CharField(max_length=30)
	# Content
	dispenser = models.IntegerField()
	nozzels = models.IntegerField()
	atg = models.BooleanField(default=True)

	def __str__(self):
		return self.site_name


class Tank(models.Model):

	zero = 0.0

	tank = models.CharField(max_length=120)
	status = models.CharField(max_length=120)
	fuelgrade = models.CharField(max_length=120)
	tankfilling = models.DecimalField(max_digits=5, decimal_places=2, default=zero)
	product = models.CharField(max_length=120)
	temperature = models.DecimalField(max_digits=8, decimal_places=4, default=zero)
	product_1 = models.CharField(max_length=120)
	water = models.CharField(max_length=120)
	tc_volume = models.CharField(max_length=120)
	dencity = models.DecimalField(max_digits=5, decimal_places=2, default=zero)
	mass = models.DecimalField(max_digits=5, decimal_places=2, default=zero)


class Company_Product(models.Model):

	label_choices = [
		('PMG', 'PMG'),
		('HSD', 'HSD'),
		('HOBC', 'HOBC'),
	]

	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	label = models.CharField(max_length=4, choices=label_choices)
	area = models.CharField(max_length=20)
	branch = models.CharField(max_length=20)
	level = models.IntegerField()

	def __str__(self):
		return str(self.company) + ' - ' + self.label
