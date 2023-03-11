from django.db import models

# Create your models here.
class Chat(models.Model):
	msg = models.CharField(max_length=100)
	time = models.DateTimeField(auto_now=True)
	group = models.ForeignKey(to='Group', on_delete=models.CASCADE)
	
	def __str__(self):
		return self.msg
	
class Group(models.Model):
	name = models.CharField(max_length=30)
	
	def __str__(self):
		return self.name