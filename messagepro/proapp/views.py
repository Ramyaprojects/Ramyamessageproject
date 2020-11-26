from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi_view(requestt):
    return HttpResponse("<h1>hi this message is from Ramya</h1>")
