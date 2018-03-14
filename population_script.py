import os
import thesportsdb
os.enviorn.setdefault('DJANGO_SETTINGS_MODULE', 'gametime.settings')

import django
django.setup()
from play.models import User, Team, Event, Comment

def populate():
