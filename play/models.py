from django.db import models

# Create your models here.
class User(models.Model):
    #I believe that IDs are automatically assigned so i'm commenting this field out for now
    #user_id = models.IntegerField(unique=True)
    username =models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30,unique=True)
    profile_pic = models.ImageField(upload_to=True,height_field=30,width_field=60,max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    #team_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=128, unique=True)
    follower = models.ForeignKey(User)
    thumbnail = models.ImageField(upload_to=False,height_field=100,width_field=200,max_length=100)

    class Meta:
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=200, unique=False,null=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=128, unique=False)
    time = models.DateTimeField(auto_now=False,auto_now_add=False)
    picture = models.ImageField(upload_to=True,height_field=100,width_field=200,max_length=100)
    description = models.TextField(max_length=300, default="None")
    host = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)

    def __str__(self):
        return self.name