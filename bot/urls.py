from django.conf.urls import url

from . import views,interface

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^callback', interface.callback),
]
