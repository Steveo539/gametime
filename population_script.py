os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gametime.settings')
import django
django.setup()
import json
import requests
import urllib
from urllib.request import urlopen
from play.models import User,Team,Comment,Event


sports = ["Soccer", "Fighting", "Basketball", "American Football", "Ice Hockey", "Rugby", "Tennis", "Cricket"]
sport_ids = {"Soccer":102,"Fighting":104,"Basketball":106,
            "American Football":107,"Ice Hockey":108,"Rugby":110,
            "Tennis":111,"Cricket":112}
API_TOKEN = "1"
API_BASE_URL = 'http://www.thesportsdb.com/api/v1/json'



def gather_leagues_by_sport():
    url = "%s/%s/all_leagues.php" % (API_BASE_URL, API_TOKEN)
    data = json.load(urlopen(url))
    leagues = data['leagues']
    for league in leagues:
        if league['strSport'] in sports:
            #print (league['strLeague'])
            gather_teams_by_league(league['idLeague'])

def gather_teams_by_league(id):
    url = "%s/%s/lookup_all_teams.php?id=%s" % (API_BASE_URL, API_TOKEN,id)
    data = json.load(urlopen(url))
    teams = data['teams']
    for team in teams:
        print(team['strTeam'])

if __name__ == '__main__':
    gather_leagues_by_sport()
