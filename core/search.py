import requests
import json

class Search():
    def __init__(self, query):
        self.headers = {
	        "X-RapidAPI-Key": "API",
	        "X-RapidAPI-Host": "spotify-scraper.p.rapidapi.com"
        }
        self.url = "https://spotify-scraper.p.rapidapi.com/v1/search"
        self.querystring = {"term":f"{query}"}

        self.trackstring = {"term":f"{query}","type":"track"}
        self.podcaststring = {"term":f"{query}","type":"podcast"}
        
    def albums(self):
        response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        self.albums = []
        for i in range(len(response.json()['albums']['items'])):
            self.albums.append([(response.json()['albums']['items'][i]['name']),
                                (response.json()['albums']['items'][i]['shareUrl']),
                                (response.json()['albums']['items'][i]['date']),
                                (response.json()['albums']['items'][i]['artists'][0]['name'])])
        return self.albums
    
    def artists(self):
        response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        self.artists = []
        for i in range(len(response.json()['artists']['items'])):
            self.artists.append([(response.json()['artists']['items'][i]['name']),
                                 (response.json()['artists']['items'][i]['shareUrl'])])
        return self.artists

    def episodes(self):
        response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        self.episodes = []
        for i in range(len(response.json()['episodes']['items'])):
            self.episodes.append([(response.json()['episodes']['items'][i]['name']),
                                  (response.json()['episodes']['items'][i]['shareUrl']),
                                  (response.json()['episodes']['items'][i]['date']),
                                  (response.json()['episodes']['items'][i]['artists']['durationText'])])
        return self.episodes

    def playlists(self):
        response = requests.get(self.url, headers=self.headers, params=self.podcaststring)
        self.playlists = []
        for i in range(len(response.json()['playlists']['items'])):
            self.playlists.append([(response.json()['playlists']['items'][i]['name']),
                                   (response.json()['playlists']['items'][i]['shareUrl']),
                                   (response.json()['playlists']['items'][i]['owner'][0]['name'])])
        return self.playlists

    def podcasts(self):
        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        self.podcasts = []
        for i in range(len(response.json()['podcasts']['items'])):
            self.podcasts.append([(response.json()['podcasts']['items'][i]['name']),
                                (response.json()['podcasts']['items'][i]['shareUrl']),
                                (response.json()['podcasts']['items'][i]['publisherName'])])
        return self.podcasts

    def tracks(self):
        response = requests.request("GET", self.url, headers=self.headers, params=self.trackstring)
        self.tracks = []
        for i in range(len(response.json()['tracks']['items'])):
            self.tracks.append([(response.json()['tracks']['items'][i]['name']),
                                (response.json()['tracks']['items'][i]['shareUrl']),
                                (response.json()['tracks']['items'][i]['durationText']),
                                (response.json()['tracks']['items'][i]['artists'][0]['name'])])
        return self.tracks

    def __str__(self):
        pass
