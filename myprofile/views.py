from django.shortcuts import render

def my_profile(request):
    return render(request, 'myprofile/my_profile.html', {})

def about_business(request):
    return render(request, 'myprofile/my_business.html', {})