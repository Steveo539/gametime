from django.contrib import admin
from play.models import UserProfile,Team,Event,Comment
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(Comment)
