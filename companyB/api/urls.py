__author__ = 'yinjun'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^find', views.find, name='find'),
    url(r'^recommend', views.recommend, name='recommend'),
]