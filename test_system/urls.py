from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home' ),
    url(r'^candidate/$', views.candidate_detail, name='candidate_detail'),
]