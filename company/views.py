from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Company, Site, Company_Product
from . forms import CompanyRegisterationForm, SiteRegisterationForm, AddProductForm

# Create your views here.
def companies(request):

	obj = Company.objects.all()

	context = {
		'obj': obj
	}

	return render(request, 'company/companies.html', context)


def sites(request, id):

	company = Company.objects.get(pk=id)

	obj = Site.objects.filter(company = company)

	if company.no_of_sites == 0:
		context = {
			'Empty': True,
			'company': company
		}

	else:
		context = {
			'obj': obj,
			'company': company
		}

	return render(request, 'company/sites.html', context)


def company_registeration(request):

	if request.method == 'POST':
		form = CompanyRegisterationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Company added successfuly !!')
			return redirect('home')

		else:
			messages.error(request, 'Form Error !!')

	else:
		form = CompanyRegisterationForm()

	context = {
		'form': form
	}

	return render(request, 'company/company_registeration.html', context)


def site_registeration(request):
	
	if request.method == 'POST':
		form = SiteRegisterationForm(request.POST)
		if form.is_valid():
			company = form.cleaned_data.get('company')
			comp_obj = Company.objects.get(company_name = company)
			comp_obj.no_of_sites += 1
			comp_obj.save()
			form.save()
			messages.success(request, 'Site added successfuly !!')
			return redirect('companies')

		else:
			messages.error(request, 'Form Error !!')

	else:
		form = SiteRegisterationForm()

	context = {
		'form': form
	}

	return render(request, 'company/site_registeration.html', context)


def add_product(request):

	if request.method == 'POST':
		form = AddProductForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Product added successfuly !!')
			return redirect('companies')

		else:
			messages.error(request, 'Form Error !!')

	else:
		form = AddProductForm()

	context = {
		'form': form
	}

	return render(request, 'company/add_product.html', context)


def company_products(request, id):

	company = Company.objects.get(pk=id)

	obj = Company_Product.objects.filter(company = company.id)

	context = {
		'obj': obj,
		'company': company
	}
	
	return render(request, 'company/company_products.html', context)


def delete_company(request, id):

	obj = Company.objects.get(pk=id)
	obj.delete()

	return redirect('home')


def edit_company(request, id):

	if request.method == "GET":
		obj = Company.objects.get(pk=id)
		form = CompanyRegisterationForm(instance = obj)

		context = {
			'form': form
		}

		return render(request, 'company/edit_company.html', context)

	else:
		obj = Company.objects.get(pk=id)
		form = CompanyRegisterationForm(request.POST, instance = obj)
		if form.is_valid():
			form.save()

		return redirect('home')







