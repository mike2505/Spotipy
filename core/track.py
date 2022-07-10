import requests
class Track():
    def __init__(self, furl):
        self.url = "https://spotify-scraper.p.rapidapi.com/v1/track/download"
        self.querystring = {"track":f"{furl}"}

        self.headers = {
            "X-RapidAPI-Key": "API",
            "X-RapidAPI-Host": "spotify-scraper.p.rapidapi.com"
        }

    def download(self):
        response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        self.down = [response.json()['youtubeVideo']['audio'][0]['url'], (response.json()['youtubeVideo']['audio'][0]['durationMs'] / 1000)]
        return self.down
