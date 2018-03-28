from django.conf.urls import url
from play import views

urlpatterns=[
url(r'^$', views.index, name='index'),
url(r'^about/', views.about, name='about'),
url(r'^signup/$', views.signup, name='signup'),
url(r'^login/', views.login_view, name='login'),
url(r'^logout/$', views.user_logout, name='user_logout'),
url(r'^profile/', views.profile, name='profile'),
url(r'^custom_event/', views.custom_event, name='custom_event'),
url(r'^create_event/', views.create_event, name = 'create_event'),
url(r'^football/', views.football, name='football'),
url(r'^american_football/', views.american_football, name='american_football'),
url(r'^basketball/', views.basketball, name='basketball'),
url(r'^ice_hockey/', views.ice_hockey, name='ice_hockey'),
url(r'^rugby/', views.rugby, name='rugby'),
url(r'^cricket/', views.cricket, name='cricket'),
url(r'^tennis/', views.tennis, name='tennis'),
url(r'^mma/', views.mma, name='mma'),
]
