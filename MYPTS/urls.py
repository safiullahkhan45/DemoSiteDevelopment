"""MYPTS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from dashboard import views as dash_views
from company import views as comp_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Dashboard Views
    path('', dash_views.dashboard, name='dashboard'),
    path('sitemonitoring', dash_views.sitemonitoring, name='sitemonitoring'),
    path('pumps', dash_views.pumps, name='pumps'),
    path('tanks', dash_views.tanks, name='tanks'),
    path('reports', dash_views.reports, name='reports'),
    path('logging', dash_views.logging, name='logging'),
    path('diagnostics', dash_views.diagnostics, name='diagnostics'),
    path('settings', dash_views.settings, name='settings'),

    # Users Views
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='dashboard/dashboard.html'), name='logout'),
    # path('profile/', user_views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    
    # Company Views
    path('company_registeration', comp_views.company_registeration, name='company_registeration'),
    path('site_registeration', comp_views.site_registeration, name='site_registeration'),
    path('add_product', comp_views.add_product, name='add_product'),
    path('companies', comp_views.companies, name='companies'),
    path('sites/<int:id>/', comp_views.sites, name='sites'),
    path('company_products/<int:id>/', comp_views.company_products, name='company_products'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    