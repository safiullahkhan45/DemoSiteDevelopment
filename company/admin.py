from django.contrib import admin
from . models import Company, Site, Tank, Company_Product

# Register your models here.
admin.site.register(Company)
admin.site.register(Site)
admin.site.register(Tank)
admin.site.register(Company_Product)