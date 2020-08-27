from django.shortcuts import render
from django.core.paginator import Paginator
from company.models import Tank, Company_Product, Company

# Create your views here.

def home(request):

    obj = Company.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(obj, 5)
    
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)

    context = {
		'obj': obj
	}

    return render(request, 'dashboard/home.html', context)

def dashboard(request):

	context = {}

	return render(request, 'dashboard/dashboard.html', context)

def sitemonitoring(request):

	context = {}

	return render(request, 'dashboard/sitemonitoring.html', context)

def pumps(request):

	context = {}

	return render(request, 'dashboard/pumps.html', context)

def tanks(request):

	obj = Tank.objects.all()

	context = {
		'obj': obj
	}

	return render(request, 'dashboard/tanks.html', context)

def reports(request):

	context = {}

	return render(request, 'dashboard/reports.html', context)

def logging(request):

	context = {}

	return render(request, 'dashboard/logging.html', context)

def diagnostics(request):

	context = {}

	return render(request, 'dashboard/diagnostics.html', context)

def settings(request):

	context = {}

	return render(request, 'dashboard/settings.html', context)
