from django.db import models
from django.contrib.auth.models import User

import datetime

# Create your models here.

#To be modified later...for now just simple ADD/DISPLAY task
'''
class ToDOList(models.Model):
	List_Id = models.CharField(max_length=255, primary_key=True)
	List_name = models.CharField(max_length=255, default='')
'''

class AddTask(models.Model):
	TaskDescription = models.TextField()
	TaskCreatedOn = models.DateTimeField()
	TaskAuthor = models.CharField(max_length=20, default='Chetan')

	def __str__(self):
		return self.TaskCreatedOn