# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	image = models.FileField(null=True)
	def __str__(self) :
		return self.title
class Comment(models.Model):
	post = models.ForeignKey('post',on_delete=models.CASCADE,related_name='comments')
	user = models.CharField(max_length=100)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.post)