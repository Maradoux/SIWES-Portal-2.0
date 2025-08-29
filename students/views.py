from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    return HttpResponse("This is where to register!")

def status(request):
    return HttpResponse("You will be accepted or rejected here! ")