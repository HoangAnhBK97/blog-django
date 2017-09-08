from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$',views.indexs,name="index"),
	url(r'^contact/$',views.contact,name="contact"),
	url(r'^info/$',views.info,name="info"),
	url(r'^register/$',views.register,name="register"),
	url(r'^login/$',auth_views.login,{'template_name':'page/login.html'},name="login"),
	url(r'^logout/$',auth_views.logout,{'next_page':'/'},name="logout")
]