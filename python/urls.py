from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.list,name="list"),
	url(r'^(?P<post_id>\d+)$',views.Post,name="post"),
]