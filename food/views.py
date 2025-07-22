from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def food(request):
    return render(request, 'food.html')

def profile(request):
    return render(request, 'profile.html')
def basetemplates(request):
    return render(request, 'basetemplates.html') 








