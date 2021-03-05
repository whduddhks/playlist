from django.shortcuts import render, redirect

def profile(request):
    return render(request, 'profile.html')

# Create your views here.
