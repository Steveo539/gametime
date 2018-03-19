import urllib.request

if __name__ == '__main__':
    url = "https://www.thesportsdb.com/images/media/team/badge/qtsqtx1473453261.png"
    urllib.request.urlretrieve(url, 'test.png')
