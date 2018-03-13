from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Testing base functionality, This is the index page")

def about(request):
    return HttpResponse("This is the About page")

def signup(request):
    return HttpResponse("This is the Signup page")

def login(request):
    return HttpResponse("This is the Login page")

def profile(request):
    return HttpResponse("This is the Profile page")

def football(request):
    return HttpResponse("This is the Football page")
def american_football(request):
    return HttpResponse("This is the American Football page")
def basketball(request):
    return HttpResponse("This is the Basketball page")
def ice_hockey(request):
    return HttpResponse("This is the Ice Hockey page")
def rugby(request):
    return HttpResponse("This is the Rugby page")
def cricket(requst):
    return HttpResponse("This is the Cricket page")
def tennis(request):
    return HttpResponse("This is the Tennis page")
def mma(request):
    return HttpResponse("This is the MMA page")
