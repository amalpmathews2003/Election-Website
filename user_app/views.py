from django.shortcuts import render
from . import views


def user_home_page(request):
	return render(request,'user_app/temp.html',{})
