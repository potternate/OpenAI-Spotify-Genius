import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Spotipy
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=os.getenv('SPOTIFY_CLIENT_ID'), client_secret=os.getenv('SPOTIFY_CLIENT_SECRET')))

# Set up Genius API
genius = lyricsgenius.Genius(os.getenv('GENIUS_API_KEY'))

# Set up OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_song_info(song_name):
    # Search for the song on Spotify
    results = spotify.search(q='track:' + song_name, type='track')

    # Extract relevant song info
    if results['tracks']['items']:
        track_info = results['tracks']['items'][0]
        artist = track_info['artists'][0]['name']
        song_title = track_info['name']
        album = track_info['album']['name']
        spotify_id = track_info['id']
        
        # Get audio features
        audio_features = spotify.audio_features([spotify_id])[0]
        danceability = audio_features['danceability']
        energy = audio_features['energy']
        loudness = audio_features['loudness']
        tempo = audio_features['tempo']

        return artist, song_title, album, spotify_id, danceability, energy, loudness, tempo
    else:
        return None

def get_lyrics(song_title, artist):
    # Search for the lyrics on Genius
    song = genius.search_song(song_title, artist)
    if song:
        return song.lyrics
    else:
        return None

def generate_blog_post(song_title, artist, lyrics, danceability, energy, loudness, tempo):
    # Generate a blog post using OpenAI
    prompt = f"Write a blog post about the song '{song_title}' by {artist}. The lyrics are:\n\n{lyrics}\n\nAdditional sound features:\nDanceability: {danceability}\nEnergy: {energy}\nLoudness: {loudness}\nTempo: {tempo}"
    try:
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": prompt}], max_tokens=5000, temperature=0.7)
        if response.choices:
            generated_blog_post = response.choices[0]['message']['content'].strip()
            return generated_blog_post
        else:
            print("Error: No response from OpenAI.")
    except Exception as e:
        print(f"Error generating blog post: {e}")

    return None



def main():
    # Prompt user for input
    song_name = input("Enter the name of a song: ")

    # Get song info from Spotify
    song_info = get_song_info(song_name)
    if song_info:
        artist, song_title, album, spotify_id, danceability, energy, loudness, tempo = song_info
        print(f"Artist: {artist}\nSong: {song_title}\nAlbum: {album}")
        print(f"Danceability: {danceability}\nEnergy: {energy}\nLoudness: {loudness}\nTempo: {tempo}")

        # Get lyrics from Genius
        lyrics = get_lyrics(song_title, artist)
        if lyrics:
            print("\nLyrics:")
            print(lyrics)

            # Generate blog post
            blog_post = generate_blog_post(song_title, artist, lyrics, danceability, energy, loudness, tempo)
            print("\nGenerated Blog Post:")
            print(blog_post)
        else:
            print("Lyrics not found.")
    else:
        print("Song not found on Spotify.")

if __name__ == "__main__":
    main()
