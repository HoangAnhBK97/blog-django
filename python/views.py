# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from python.models import post,Comment 
from django.http import Http404,HttpResponseRedirect
from home.forms import *


# Create your views here.
def list(request):
	Data = {
		'Posts':post.objects.all().order_by("-date")[:10]
	}
	return render(request,'python/python.html',Data)

def Post(request,post_id):
	if request.method == "POST" :
		form = CommentForm(request.POST)
		Post = get_object_or_404(post,pk=post_id)
		if form.is_valid() :
			comment = form.save(commit=False)
			comment.user = request.user 
			comment.post = Post 
			comment.save()
			return HttpResponseRedirect(post_id)
	form = CommentForm()
	try :
		post.objects.get(pk=post_id)
	except post.DoesNotExist :
		raise Http404("Bài viết không tồn tại hoặc đã bị xóa !")
	return render(request,'python/post.html',{'Post':post.objects.get(pk=post_id),'form':form})
