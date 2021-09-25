from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class VoterModel(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	#name=models.CharField(max_length=200)
	roll_no=models.CharField(max_length=20,null=True,blank=True)
	email=models.EmailField(null=True)
	is_voted=models.BooleanField(default=False)
	def __str__(self):
		return self.roll_no

@receiver(post_save,sender=User)
def update_voter_model(sender,instance,created,**kwargs):
	if created:
		VoterModel.objects.create(user=instance,pk=instance.id)
	try:
		instance.votermodel.save()	
	except:
		VoterModel.objects.create(user=instance)


class CandidateModel(models.Model):

	position_choices=(
		("1","Chairman"),
		("2",'Secretary'),
		("3","Member"))
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	#name=models.CharField(max_length=200)
	roll_no=models.CharField(max_length=20,null=True,blank=True)
	email=models.EmailField(null=True)
	description=models.TextField(blank=True,null=True)
	position=models.CharField(max_length=200,choices=position_choices,default='1')
	image=models.ImageField(upload_to="images/",blank=True,null=True)
	def __str__(self):
		return self.user.first_name

@receiver(post_save,sender=User)
def update_candidate_model(sender,instance,created,**kwargs):
	if created:
		CandidateModel.objects.create(user=instance,pk=instance.id)
	try:
		instance.candidatemodel.save()	
	except:
		CandidateModel.objects.create(user=instance)


class InvigilaterModel(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	candidates=models.ManyToManyField(CandidateModel)
	voters=models.ManyToManyField(VoterModel)
	def __str__(self):
		return self.user.first_name

@receiver(post_save,sender=User)
def update_invigilater_model(sender,instance,created,**kwargs):
	if created:
		InvigilaterModel.objects.create(user=instance,pk=instance.id)
	try:
		instance.invigilatermodel.save()	
	except:
		InvigilaterModel.objects.create(user=instance)
