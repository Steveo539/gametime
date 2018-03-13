from django.db import models

# Create your models here.
class Team(models.Model):
    id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class User(models.Model:
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=264, unique=False)
    sport =
    host = models.OneToOneField(User)

    def __str__(self):
        return self.name
