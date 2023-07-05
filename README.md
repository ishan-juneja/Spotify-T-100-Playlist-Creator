# Spotify-T-100-Playlist-Creator
Creates a Spotify playlist filled with the top 100 songs of any day requested by the user.

## Structure
- `main.py` behaves as the nucleus and runs the entirety of the program
  
## Dependencies & Configurations
1. The [Spotipy API](https://spotipy.readthedocs.io/en/2.22.1/) used for accessing our Spotify account to create our playlist
   - Retrieve your **client_id** & **client_passsword** after creating an account and making an application in your account.
   - Add to `main.py`
2. The [Beautiful Soup Library](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) used for web scraping the songs off of the Billboard's Top 100 Chart of the specified day.
## Demo
The program inquires about which day we want our playlist.
<img width="731" alt="Screenshot 2023-07-05 at 8 47 41 AM" src="https://github.com/ishan-juneja/Spotify-T-100-Playlist-Creator/assets/69048541/c92f2cbc-7d70-46a7-95f3-9f41611e7427">

The program then produces the playlist for us in our account!
[Playlist Link](https://open.spotify.com/playlist/6swcVagGpxowAG3OSuMMK2?si=a0e4d452658f4813)
<img width="1249" alt="Screenshot 2023-07-05 at 8 48 50 AM" src="https://github.com/ishan-juneja/Spotify-T-100-Playlist-Creator/assets/69048541/4bdd6e4b-3e22-42f5-a799-9e81590af2e1">
