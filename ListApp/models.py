from django.db import models
import datetime

# Create your models here.

#To be modified later...for now just simple ADD/DISPLAY task
'''
class ToDOList(models.Model):
	List_Id = models.CharField(max_length=255, primary_key=True)
	List_name = models.CharField(max_length=255, default='')
'''



class AddTask(models.Model):
#	Task_Id = models.CharField(max_length=255, primary_key=True)
	TaskDescription = models.TextField()
	TaskCreatedOn = models.DateTimeField(auto_now_add=True)
	
