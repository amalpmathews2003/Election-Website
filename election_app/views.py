from django.shortcuts import render

def home_page(request):
	return render(request,'election_app/home_page.html',{})