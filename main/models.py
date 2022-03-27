from django.db import models

class contact(models.Model):
	name=models.CharField(max_length=200)
	mobile=models.CharField(max_length=14)
	subject=models.CharField(max_length=400)
	email=models.CharField(max_length=200)
	message=models.CharField(max_length=1000)

class applyhere(models.Model):
	emailid=models.TextField(null=True)
	profile=models.TextField(null=True)
	linkedin=models.TextField(null=True)
	ceo=models.TextField(null=True)
	startup=models.TextField(null=True)
	weblink=models.TextField(null=True)
	estdate=models.TextField(null=True)
	targetmarket=models.TextField(null=True)
	targetsize=models.TextField(null=True)
	funding=models.TextField(null=True)
	investors=models.TextField(null=True)
	monthrevenue1=models.TextField(null=True)
	monthrevenue2=models.TextField(null=True)
	monthrevenue3=models.TextField(null=True)
	presentation=models.TextField(null=True)
	