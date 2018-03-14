from django.contrib import admin
from play.models import User,Team,Event,Comment
# Register your models here.
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(Comment)
