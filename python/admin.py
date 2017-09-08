# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from python.models import post,Comment
# Register your models here.
admin.site.register(post)
admin.site.register(Comment)