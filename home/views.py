from django.shortcuts import render

# Create your views here.

def index_home(request):
    return render(request, 'home/index_home.html')