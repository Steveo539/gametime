import json
import requests
import urllib
from urllib.request import urlopen
if __name__ == '__main__':
    url = "https://newsapi.org/v2/top-headlines?sources=bbc-sport&apiKey=f40bc449adc04fd48ed5fc6e292831f5"
    data = json.load(urlopen(url))
    for i in range(0,len(data['articles'])):
        print(data['articles'][i]['title'])
        print(data['articles'][i]['description'])
        print(data['articles'][i]['url'])
        print(data['articles'][i]['urlToImage'])
        print(data['articles'][i]['publishedAt'])
