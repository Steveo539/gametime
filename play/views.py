from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from play.forms import UserForm, UserProfileForm, EventForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return render(request, 'play/index.html', context={})

def about(request):
    return render(request, 'play/about.html', context={})

def signup(request):

	registered = False

	if request.method == 'POST':

		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			registered = True

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,'play/signup.html',{'user_form': user_form,'profile_form': profile_form,'registered': registered})

def login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')


		try:
			user = User.objects.get(username = username)
		except User.DoesNotExist:
			return HttpResponse("Invalid username")

		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				return HttpResponse("<p>Welcome " + username + "!</p><a href=\"play/\">Return to home</a>")

			else:
				return HttpResponse("Your Gametime account is disabled.")

		elif username != username:
			print("Invalid username: {0}".format(username))
			return HttpResponse("Invalid username supplied.")

		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid password")

	else:
		return render(request, 'play/login.html', {})


def profile(request):
    return HttpResponse("This is the Profile page")

def custom_event(request):
	return render(request, 'play/custom_event.html', context={})

def create_event(request):

	if request.method == 'POST':
		event_form = EventForm(data=request.POST)

		if event_form.is_valid():

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			event = event_form.save()

		else:
			print(event_form.errors)
	else:
		event_form = EventForm()

	return render(request, 'play/create_event.html', context={"event_form": event_form})

def football(request):

    context = {
		"leagues":{"BPL":["Man Utd","Arsenal", "Swansea"],"SPL":["Celtic", "Kilmarnock"],"NIFL":["Cville", "Glenavon"]},
		"sources":"bbc-sport,talksport,the-sport-bible",
		"keywords":"football",
	}

    return render(request, 'play/football.html', context)

def american_football(request):

	context = {
		"sources":"nfl-news",
		"keywords":"",
	}

	return render(request, 'play/american_football.html', context)

def basketball(request):

	context = {
		"sources":"",
		"keywords":"",
	}

	return render(request, 'play/basketball.html', context)

def ice_hockey(request):

	context = {
		"sources":"",
		"keywords":"",
	}

	return render(request, 'play/ice_hockey.html', context)

def rugby(request):

	context = {
		"sources":"bbc-sport,talksport,the-sport-bible",
		"keywords":"rugby",
	}

	return render(request, 'play/rugby.html', context)

def cricket(request):

	context = {
		"sources":"bbc-sport,talksport,the-sport-bible",
		"keywords":"cricket",
	}

	return render(request, 'play/cricket.html', context)

def tennis(request):

	context = {
		"sources":"bbc-sport,talksport,the-sport-bible",
		"keywords":"tennis",
	}

	return render(request, 'play/tennis.html', context)

def mma(request):

	context = {
		"sources":"",
		"keywords":"",
	}

	return render(request, 'play/mma.html', context)
