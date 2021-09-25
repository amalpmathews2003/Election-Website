from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import * 

def user_home_page(request):
	return render(request,'user_app/temp.html',{})


class VoterCreateView(generic.CreateView):
	model=VoterModel
	#fields=['name','roll_no','email']
	fields="__all__"
	success_url=reverse_lazy('home-page')


class CandidateCreateView(generic.CreateView):
	model=CandidateModel
	fields=['name','roll_no','email','description','position','image']
	success_url=reverse_lazy('home-page')

class InvigilaterCreateView(generic.CreateView):
	model=InvigilaterModel
	fields=['name']
	success_url=reverse_lazy('home-page')