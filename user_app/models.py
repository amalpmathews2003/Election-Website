from django.db import models
from django.contrib.auth.models import User

class VoterModel(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	#name=models.CharField(max_length=200)
	roll_no=models.CharField(max_length=20,unique=True)
	email=models.EmailField(unique=True)
	is_voted=models.BooleanField(default=False)
	def __str__(self):
		return self.name

class CandidateModel(models.Model):

	position_choices=(
		("1","Chairman"),
		("2",'Secretary'),
		("3","Member"))
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	#name=models.CharField(max_length=200)
	roll_no=models.CharField(max_length=20,unique=True)
	email=models.EmailField(unique=True)
	description=models.TextField(blank=True,null=True)
	position=models.CharField(max_length=200,choices=position_choices,default='1')
	image=models.ImageField(upload_to="images/",blank=True,null=True)
	def __str__(self):
		return self.name


class InvigilaterModel(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	candidates=models.ManyToManyField(CandidateModel)
	voters=models.ManyToManyField(VoterModel)
	def __str__(self):
		return self.name