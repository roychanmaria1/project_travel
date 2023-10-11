from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Name

# Create your views here.
def demo(request):
    obj = Place.objects.all()
    return render(request,"index.html",{'result':obj})

def sample(request):
    obj1 = Name.objects.all()
    return render(request,"index.html",{'results':obj1})



