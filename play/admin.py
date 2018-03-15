from django.contrib import admin
from play.models import Team, User, Comment, Event
# Register your models here.
admin.site.register(Team)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Event)
