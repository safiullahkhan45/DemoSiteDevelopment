from django import forms
from .models import Company, Site, Company_Product

class CompanyRegisterationForm(forms.ModelForm):

	class Meta:
		model = Company
		fields = [
			'company_owner',
			'company_name',
			'business_type',
			'contact_number',
			'email',
			'address',
		]


class SiteRegisterationForm(forms.ModelForm):

	class Meta:
		model = Site
		fields = '__all__'


class AddProductForm(forms.ModelForm):

	class Meta:
		model = Company_Product
		fields = [
			'company',
			'label',
			'area',
			'branch',
			'level',
		]
