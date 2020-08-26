from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required
from . models import Profile
from .forms import UserRegistrationForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


# @login_required
# def profile(request):

#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()

#     else:
#         form = ProfileUpdateForm(
#                     initial= {
#                     'email': request.user.email,
#                     'address': request.user.address,
#                     'mobile_number': request.user.mobile_number
#                 }
#             )

#     context = {
#         'form': form
#     }

#     return render(request, 'users/profile.html', context)

