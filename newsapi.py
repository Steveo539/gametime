import json
import requests
import urllib

api_token = 'f40bc449adc04fd48ed5fc6e292831f5'
api_url_base = 'http://www.thesportsdb.com/api/v1/json'

headers = {'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(api_token)}

def get_account_info():
    url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=f40bc449adc04fd48ed5fc6e292831f5')
    response = requests.get(url)
    print(response.json())
    # api_url = '{0}account'.format(api_url_base)
    #
    # response = requests.get(api_url, headers=headers)
    #
    # if response.status_code == 200:
    #     return json.loads(response.content.decode('utf-8'))
    # else:
    #     print("oops!")
    #     print(response.status_code)

if __name__ == "__main__":
    get_account_info()
