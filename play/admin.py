from django.contrib import admin
from play.models import Team,Event,Comment, UserProfile,Article
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(Article)
