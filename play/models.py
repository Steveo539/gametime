from django.db import models

# Create your models here.
class UserProfile(models.Model):
    #I believe that IDs are automatically assigned so i'm commenting this field out for now
    #user_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30,unique=True)
    profile_pic = models.ImageField(upload_to=True,height_field=30,width_field=60,max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    #team_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=128, unique=True)
    sport = models.CharField(max_length=30, unique=False, default="N/A")
    country = models.CharField(max_length=50, unique=False, default="N/A")
    league = models.CharField(max_length=100, unique=False, default="N/A")
<<<<<<< HEAD
    follower = models.ForeignKey(UserProfile, null=True)
=======
    follower = models.ForeignKey(User, null=True)
>>>>>>> e7d4a08d95c5dac7f7d7760679505a00e6e31f9c
    thumbnail = models.CharField(max_length=250, default="N/A")

    class Meta:
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(UserProfile)
    text = models.CharField(max_length=200, unique=False,null=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=128, unique=False)
    time = models.DateTimeField(auto_now=False,auto_now_add=False)
    picture = models.ImageField(upload_to=True,height_field=100,width_field=200,max_length=100)
    description = models.TextField(max_length=300, default="None")
    host = models.ForeignKey(UserProfile)
    comment = models.ForeignKey(Comment)

    def __str__(self):
        return self.name
