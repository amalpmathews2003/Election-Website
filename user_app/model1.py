from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class VoterModel(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	roll_no=models.CharField(max_length=20,null=True)
	is_voted=models.BooleanField(default=False)
	def __str__(self):
		if isinstance(self.roll_no,str):
			return self.roll_no
		else:
			return 'error'
# @receiver(post_save,sender=User)
# def update_voter_model(sender,instance,created,**kwargs):
# 	if created:
# 		VoterModel.objects.create(user=instance,pk=instance.id)
# 	try:
# 		instance.votermodel.save()	
# 	except:
# 		VoterModel.objects.create(user=instance)
