import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gametime.settings')
import django
django.setup()
import json
import requests
import urllib
from urllib.request import urlopen
from play.models import User,Team,Comment,Event,Article

sports = ["Soccer", "Fighting", "Basketball", "American Football", "Ice Hockey", "Rugby", "Tennis", "Cricket"]
sport_ids = {"Soccer":102,"Fighting":104,"Basketball":106,
            "American Football":107,"Ice Hockey":108,"Rugby":110,
            "Tennis":111,"Cricket":112}
API_TOKEN = "1"
API_BASE_URL = 'http://www.thesportsdb.com/api/v1/json'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAMETIME_DIR = os.path.join(BASE_DIR, 'gametime')
STATIC_DIR = os.path.join(GAMETIME_DIR, 'static')
LOGOS_DIR = os.path.join(STATIC_DIR,'logos')
ARTICLES_DIR = os.path.join(STATIC_DIR,'articles')


def download_image(name, url):
    cwd = os.getcwd()
    os.chdir(LOGOS_DIR)
    urllib.request.urlretrieve(url, name+'.png')
    os.chdir(cwd)
    return (name+'.png')

def download_image_article(name, url):
    cwd = os.getcwd()
    os.chdir(ARTICLES_DIR)
    urllib.request.urlretrieve(url, name+'.jpg')
    os.chdir(cwd)
    return (name+'.jpg')

def gather_articles():
    url = "https://newsapi.org/v2/top-headlines?sources=bbc-sport&apiKey=f40bc449adc04fd48ed5fc6e292831f5"
    data = json.load(urlopen(url))
    for i in range(0,len(data['articles'])):
        title = data['articles'][i]['title']
        description = data['articles'][i]['description']
        url = data['articles'][i]['url']
        img = data['articles'][i]['urlToImage']
        pub  =data['articles'][i]['publishedAt']
        #print(title + " " + description + " " + url + " " + img + " " + pub + "\n")
        add_article(title, description, url, img, pub)


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
        #print(data['teams'][0])
    for team in teams:
        #print(team['strTeamBadge'])
        add_team(team['strTeam'], team['strSport'], team['strCountry'], team['strLeague'], team['strTeamBadge'])

def add_article(t_title, t_desc, t_url,t_urlToImage,t_publishedAt):
    a = Article.objects.get_or_create(title=t_title)[0]
    a.url = t_url
    a.description = t_desc
    a.image = download_image_article(str(a.id),t_urlToImage)
    a.publication_date = t_publishedAt
    a.save()
    return a

def add_team(t_name, t_sport, t_country, t_league, t_thumbnail):
    t = Team.objects.get_or_create(name=t_name)[0]
    t.sport = t_sport
    t.country = t_country
    t.league = t_league
    if t_thumbnail != None: t.thumbnail = download_image(t_name,t_thumbnail)
    t.save()
    return t

if __name__ == '__main__':
    print("Starting 'play' population script...Gathering articles\n")
    gather_articles()
    print("Articles gathered...collecting teams\n")
    gather_leagues_by_sport()
    print("Finished!")
