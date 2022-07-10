from search import Search
from track import Track
import os
import time
import vlc

class SpotiPy():
    def __init__(self, query):
        self.query = query
    
    def get_track_url(self, choice):
        global name
        url = Search(self.query)
        k = 1
        names =[]
        for i in url.tracks():
            print(f"{k}. Name: {i[0]}\n    Duration: {i[2]}\n    Artist: {i[3]}")
            k += 1
            names.append(i[0])
        print("Enter number of song to play: ", end='')
        num = int(input())
        name = names[num - 1]
        return url.tracks[num-1][1]


if __name__ == '__main__':
    exit_ch = ''
    while exit_ch.lower() != 'n':
        os.system('clear')
        search = str(input('Enter song to search for: '))
        try:
            song = SpotiPy(search)
            get_song = Track(song.get_track_url('track'))
            p = vlc.MediaPlayer(get_song.download()[0])
            p.audio_set_volume(100)
            p.play()
            os.system('clear')
            time.sleep(1)
            os.system('clear')
            print(f'Playing: {name}')
            time.sleep(get_song.download()[1])
            exit_ch = str(input('Search again? (Y/n): '))
        except:
            print("Cant find song :C")
            exit_ch = str(input('Search again? (Y/n): '))