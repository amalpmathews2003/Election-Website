from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User



class CandidateModel(models.Model):
	position_choices=(
		("1","Chairman"),
		("2",'Secretary'),
		("3","Member"))
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	roll_no=models.CharField(max_length=20)
	description=models.TextField(blank=True,null=True)
	position=models.CharField(max_length=200,choices=position_choices,default='1')
	image=models.ImageField(upload_to="images/",blank=True,null=True)
	votes=models.IntegerField(default=0)
	is_validated=models.BooleanField(default=0)
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

