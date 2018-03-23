from django import forms
from django.contrib.auth.models import User
from play.models import Team, UserProfile, Event

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username',  'password')

class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ( 'picture',)

class EventForm(forms.ModelForm):

	class Meta:
		model = Event
		exclude = ('comment',)
