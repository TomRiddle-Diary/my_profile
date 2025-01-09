from django.shortcuts import render

def my_profile(request):
    return render(request, 'myprofile/index.html', {})

def my_business(request):
    return render(request, 'myprofile/my_business.html', {})