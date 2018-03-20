from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
class Team(models.Model):
    #team_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=128, unique=True)
    sport = models.CharField(max_length=30, unique=False, default="N/A")
    country = models.CharField(max_length=50, unique=False, default="N/A")
    league = models.CharField(max_length=100, unique=False, default="N/A")
    #follower = models.ForeignKey(UserProfile, null=True)
    thumbnail = models.CharField(max_length=250, default="N/A")

    class Meta:
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name

class Comment(models.Model):
    #user = models.ForeignKey(UserProfile)
    text = models.CharField(max_length=200, unique=False,null=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=128, unique=False)
    time = models.DateTimeField(auto_now=False,auto_now_add=False)
    picture = models.ImageField(upload_to=True,height_field=100,width_field=200,max_length=100)
    description = models.TextField(max_length=300, default="None")
    #host = models.ForeignKey(UserProfile)
    comment = models.ForeignKey(Comment)

    def __str__(self):
        return self.name
