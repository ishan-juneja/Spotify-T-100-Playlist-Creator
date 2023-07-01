from bs4 import BeautifulSoup
import requests, os
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

client_id = os.environ['CLIENT_ID']
client_password = os.environ['CLIENT_PASSWORD']
redirect_uri = os.environ['REDIRECT_URI']
#
travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

website_info = requests.get(f"https://www.billboard.com/charts/hot-100/{travel_date}/")
# print(website_info.text)

soup = BeautifulSoup(website_info.text, "html.parser")

t_100_songs = []
artists_names = []

#retrieving the first song and artist which have a different class title
t_100_songs.append(soup.find(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet").string.strip())

artists_names.append(soup.find(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet").text.strip())

#getting the rest off the 99 songs
for row in soup.findAll(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"):
    t_100_songs.append(row.text.strip())

for row in soup.findAll(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"):
    artists_names.append(row.text.strip())


# Spotify Authentication
sp_auth = spotipy.oauth2.SpotifyOAuth(client_id=client_id, client_secret=client_password, redirect_uri=redirect_uri,
                                      scope="playlist-modify-private", cache_path="token.txt")
sp = spotipy.Spotify(auth_manager=sp_auth)


my_playlist = sp.user_playlist_create(user="bolder101", name=f"Top 100 Songs From {travel_date}", public=False, collaborative=False, description=f'This playlist lists the top 100 songs from {travel_date}')

user_id = sp.current_user()['id']
for i in range(0,100):
    artist = artists_names[i]
    track = t_100_songs[i]
    market = "US"
    query = f'{track} {artist}'
    track_info = sp.search(q=f"track:{track} year:{travel_date[0:4]}", type='track')
    try:
        uri = track_info["tracks"]["items"][0]["uri"]
        sp.playlist_add_items(playlist_id=my_playlist["id"],items=[uri])
    except IndexError:
        print(f"{track} doesn't exist in Spotify. Skipped.")



#sp.playlist_add_items(playlist_id, items, position=None)





