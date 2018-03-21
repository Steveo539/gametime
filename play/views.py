from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from play.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
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

		#Profile form is invalid for some reason
		#Error message says profile_pic is required but I am unable to upload one
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
				login(request, user)
				return HttpResponseRedirect(reverse('index'))

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

def football(request):

    context={"leagues":{"BPL":["Man Utd","Arsenal", "Swansea"],"SPL":["Celtic", "Kilmarnock"],"NIFL":["Cville", "Glenavon"]},
			 "keywords":"+football",}

    return render(request, 'play/football.html', context)

def american_football(request):

	context = {"keywords":"+american+football"}

	return render(request, 'play/american_football.html', context)

def basketball(request):

	context = {"keywords":"+basketball"}

	return render(request, 'play/basketball.html', context)

def ice_hockey(request):

	context = {"keywords":"+ice+hockey"}

	return render(request, 'play/ice_hockey.html', context)

def rugby(request):

	context = {"keywords":"+rugby"}

	return render(request, 'play/rugby.html', context)

def cricket(request):

	context = {"keywords":"+cricket"}

	return render(request, 'play/cricket.html', context)

def tennis(request):

	context = {"keywords":"+tennis"}

	return render(request, 'play/tennis.html', context)

def mma(request):

	context = {"keywords":"+mma"}

	return render(request, 'play/mma.html', context)
