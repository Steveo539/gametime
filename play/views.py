from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from play.forms import UserForm, UserProfileForm
# Create your views here.
def index(request):
    return render(request, 'play/index.html', context={})

def about(request):
    return render(request, 'play/about.html', context={})

def signup(request):
<<<<<<< HEAD

	registered = False
	
	if request.method == 'POST':
		
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		
		#Profile form is invalid for some reason
		#Error message says profile_pic is required but I am unable to upload one
		if user_form.is_valid() and profile_form.is_valid():
			
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']
			profile.save()
			registered = True
		
		else:
			print(user_form.errors, profile_form.errors)
	
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
		
	return render(request,'play/signup.html',{'user_form': user_form,'profile_form': profile_form,'registered': registered})

def login(request):
    return render(request, 'play/login.html',context={})

=======
    return render(request, 'play/signup.html',context={})

def login(request):
    return render(request, 'play/login.html',context={})
>>>>>>> e7d4a08d95c5dac7f7d7760679505a00e6e31f9c

def profile(request):
    return HttpResponse("This is the Profile page")

def football(request):
    
<<<<<<< HEAD
    context={"leagues":{"BPL":["Man Utd","Arsenal", "Swansea"],"SPL":["Celtic", "Kilmarnock"],"NIFL":["Cvile", "Glenavon"]}}
=======
    context={"leagues":["BPL","SPL", "NIFL"]}
>>>>>>> e7d4a08d95c5dac7f7d7760679505a00e6e31f9c

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
