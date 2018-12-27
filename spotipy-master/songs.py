import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import json

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'Weezer'

client_id = "CLIENT_ID"
client_secret = "CLIENT_SECRET_ID"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

##result = sp.search(search_str)
##pprint.pprint(result)
#pprint.pprint(len(result))

print("+++++++++++============================")

query_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
##query_list = ['a']
artists_list2 = []
image = ''
total = 0
data =[]
outfile = open('data.txt', 'w')
def tracks(results):
##    for x in range(0, len(artists_list)):
    for i, t in enumerate(results):
          song_name = t['name']
          song_popularity = t['popularity']
          album = sp.album(t['album']['uri'])
          album_name = album['name']
          album_genres = album['genres']
          artists = sp.artist(t['artists'][0]['uri'])
          artist_name = artists['name']
          album_genres = artists['genres']
          if len(album['images']) > 0:
              image = album['images'][0]['url']
          else:
              image = 'https://wallpaperbrowse.com/media/images/i_love_music_2-wallpaper-7680x4800.jpg'
          mmm =0
          for k in artists_list2:
              if k == t['artists'][0]['uri']:
                  mmm =1
                  break
          if mmm == 0:
              artists_list2.append(t['artists'][0]['uri'])
          mmm =0
          related = sp.artist_related_artists(t['artists'][0]['uri'])
          for artist in related['artists']:
              for k in artists_list2:
                  if k == artist['uri']:
                      mmm =1
                      break
              if mmm == 0:
                  artists_list2.append(artist['uri'])

          data2 ={}
          global total
          mmm =0
          for k in data:
              if k['title'] == song_name:
                  mmm =1
                  break
          if mmm == 0:
              data2.update({'id':total,
                       'title':song_name,
                       'popularity':song_popularity,
                       'artist':artist_name,
                       'genres':album_genres,
                       'album' : album_name,
                       'image' : image
                       })
              data.append(data2)
              total = total+1

for mm in query_list:
    results = sp.search(q=mm, limit=50)
    tracks(results['tracks']['items'])


# urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
#
# response = sp.artist_top_tracks(urn)
# print(response)
m =0
while total < 10000:
    if m >= len(artists_list2):
        break
    response = sp.artist_top_tracks(artists_list2[m])
    tracks(response['tracks'])
    m = m+1
json.dump(data, outfile)

print(total)







#
# urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
#
# artist = sp.artist_top_tracks(urn)
#
# pprint.pprint(artist['tracks'][0]['album']['images'][1]['url'])
