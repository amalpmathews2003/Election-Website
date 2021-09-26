from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import *
from .models import * 

def user_home_page(request):
	return render(request,'user_app/temp.html',{})


def declare_results(request):
	all_candidates=CandidateModel.objects.all()
	member_candidates=all_candidates.filter(position="3",is_validated=1)
	secretary_candidates=all_candidates.filter(position="2",is_validated=1)
	chairman_candidates=all_candidates.filter(position="1",is_validated=1)

	member_candidates=member_candidates.order_by('-votes')[:3]
	secretary_candidates=secretary_candidates.order_by('-votes')[:3]
	chairman_candidates=chairman_candidates.order_by('-votes')[:3]
	return render(request,'user_app/declare_page.html',
		{"member_candidates":member_candidates,
		"chairman_candidates":chairman_candidates,
		"secretary_candidates":secretary_candidates
		})

# def redirect(request,url=None):
# 	print(url)
# 	return redirect('www.nitc.ac.in')

def start_voting(request):
	if not request.user.is_authenticated:
		return redirect('login-voter')
	if request.user.is_voted:
		return redirect('home-page')
	if request.method=="POST":
		form=VotingForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data['eg']
			data=data[:-1]
			datas=data.split(',')
			for data in datas:
				data=data.split(":")
				member=CandidateModel.objects.get(roll_no=data[1])
				member.votes+=1
				member.save()
			return redirect('home-page')
	else:
		form=VotingForm()
		r=CandidateModel.objects.all()
		member_candidate=CandidateModel.objects.filter(position="3",is_validated=1)
		secretary_candidate=CandidateModel.objects.filter(position="2",is_validated=1)
		chairman_candidate=CandidateModel.objects.filter(position="1",is_validated=1)
		return render(request,'election_app/temp.html',
			{"member_candidate":member_candidate,
			"secretary_candidate":secretary_candidate,
			"chairman_candidate":chairman_candidate,
			"form":form})	

def confirm_poll(request):
	return render()
def login_user(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('home-page')
		else:
			return redirect('login-voter')
	else:
		return render(request,'user_app/temp.html',{})


def logout_user(request):
	logout(request)
	return redirect('home-page')


def register_voter(request):
	if request.method=="POST":
		form=RegisterVoterForm(request.POST,request.FILES)
		if form.is_valid():
			user=form.save()
			#VoterModel.objects.create(user=user,roll_no=form.cleaned_data.get('roll_no'))
			print(user)
			#print(dir(user))
			user.votermodel.roll_no=form.cleaned_data.get('roll_no')
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
