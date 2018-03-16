from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'play/index.html', context={})

def about(request):
    return render(request, 'play/about.html', context={})

def signup(request):
    return render(request, 'play/signup.html',context={})

def login(request):
    return render(request, 'play/login.html',context={})

def profile(request):
    return HttpResponse("This is the Profile page")

def football(request):
    
    context={"leagues":["BPL","SPL", "NIFL"]}

    return render(request, 'play/football.html', context)

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
