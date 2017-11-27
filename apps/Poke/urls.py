from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index ),
    url(r'^pokes$', views.dash),
    url(r'^create$', views.create),
]