from django.conf.urls import url

from . import interface

urlpatterns = [
	url(r'^callback-line', interface.callback_line),
]
