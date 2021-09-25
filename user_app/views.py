from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import *
from .models import * 

def user_home_page(request):
	return render(request,'user_app/temp.html',{})


def logout_user(request):
	logout(request)
	return redirect('home page')


def register_voter(request):
	if request.method=="POST":
		form=RegisterVoterForm(request.POST,request.FILES)
		if form.is_valid():
			user=form.save()
			user.votermodel.roll_no=form.cleaned_data.get('roll_no')
			user.votermodel.email=form.cleaned_data.get('email')
			user.save()
			password=form.cleaned_data.get('password1')
			user=authenticate(username=user.username,password=password)
			login(request,user)
			return redirect('home-page')
	else:
		form=RegisterVoterForm()	
	return render(request,'user_app/votermodel_form.html',{'form':form})

def register_candidate(request):
	if request.method=="POST":
		form=RegisterCandidateForm(request.POST,request.FILES)
		if form.is_valid():
			user=form.save()
			user.candidatemodel.email=form.cleaned_data.get('email')
			user.candidatemodel.roll_no=form.cleaned_data.get('roll_no')
			user.candidatemodel.description=form.cleaned_data.get('description')
			user.candidatemodel.position=form.cleaned_data.get('position')
			user.candidatemodel.image=form.cleaned_data.get('image')
			password=form.cleaned_data.get('password1')
			user.save()
			user=authenticate(username=user.username,password=password)
			login(request,user)
			return redirect('home-page')
	else:
		form=RegisterCandidateForm()	
	return render(request,'user_app/candidatemodel_form.html',{'form':form})

def register_invigilater(request):
	if request.method=="POST":
		form=RegisterInvigilaterForm(request.POST,request.FILES)
		if form.is_valid():
			user=form.save()
			password=form.cleaned_data.get('password1')
			user.save()
			user=authenticate(username=user.username,password=password)
			login(request,user)
			return redirect('home-page')
	else:
		form=RegisterInvigilaterForm()	
	return render(request,'user_app/candidatemodel_form.html',{'form':form})
