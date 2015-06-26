from django.db import models

# Create your models here.
class ToDOList(models.Model):
	List_Id = models.CharField(max_length=255, primary_key=True)
	List_name = models.CharField(max_length=255, default='')

class ListTask(models.Model):
	Task_Id = models.CharField(max_length=255, primary_key=True)
	Description = models.TextField()
	Created = models.DateTimeField()
	
