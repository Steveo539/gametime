from django.conf.urls import url
from basic import views

urlpatterns=[
url(r'^$', views.index, name='index'),
url(r'^about/', views.about, name='about'),
url(r'^signup/', views.signup, name='signup'),
url(r'^login/', views.login, name='login'),
url(r'^profile/', views.profile, name='profile'),
url(r'^football/', views.football, name='football'),
url(r'^american_football/', views.american_football, name='american_football'),
url(r'^basketball/', views.basketball, name='basketball'),
url(r'^ice_hockey/', views.ice_hockey, name='ice_hockey'),
url(r'^rugby/', views.rugby, name='rugby'),
url(r'^cricket/', views.cricket, name='cricket'),
url(r'^tennis/', views.tennis, name='tennis'),
url(r'^mma/', views.mma, name='mma'),

]
