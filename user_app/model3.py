from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class InvigilaterModel(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	# candidates=models.ManyToManyField(CandidateModel)
	# voters=models.ManyToManyField(VoterModel)
	#candidates=models.ForeignKey(CandidateModel,on_delete=models.CASCADE)
	#voters=models.ForeignKey(VoterModel,on_delete=models.CASCADE)
	def __str__(self):
		if isinstance(self.roll_no,str):
			return self.user.first_name
		else:
			return 'error'

@receiver(post_save,sender=User)
def update_invigilater_model(sender,instance,created,**kwargs):
	if created:
		InvigilaterModel.objects.create(user=instance,pk=instance.id)
	try:
		instance.invigilatermodel.save()	
	except:
		InvigilaterModel.objects.create(user=instance)
