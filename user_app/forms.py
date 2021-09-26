from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import models
from django.contrib.auth.models import User


class VotingForm(forms.Form):
	eg=forms.CharField(max_length=500)
	eg.widget=forms.TextInput(attrs={'type':'hidden'})
	class Meta:
		fields="__all__"

class RegisterVoterForm(UserCreationForm):
	roll_no=forms.CharField(max_length=20)
	class Meta:
		model=User
		fields=('username','first_name','last_name','email','roll_no'
			,'password1','password2')

class RegisterCandidateForm(UserCreationForm):
	roll_no=forms.CharField(max_length=20)
	position_choices=(
		("1","Chairman"),
		("2",'Secretary'),
		("3","Member"))
	description=forms.CharField(max_length=200)
	position=forms.ChoiceField(choices=position_choices)
	image=forms.ImageField()
	class Meta:
		model=User
		fields=('username','first_name','last_name','email','roll_no',
			'password1','password2','position','description','image')

class RegisterInvigilaterForm(UserCreationForm):
	class Meta:
		model=User
		fields=('username','first_name','last_name','email'
			,'password1','password2')