# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class index(models.Model):
	body = models.TextField()
	image = models.FileField(null = True)

