from django.conf.urls import url
from basic import views

urlpatterns=[
url(r'^$', views.index, name='index'),
]
