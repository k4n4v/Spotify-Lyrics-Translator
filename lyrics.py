import lyricsgenius
import os
from dotenv import load_dotenv
from deep_translator import GoogleTranslator

load_dotenv()

client_access_token = os.getenv("GENIUS_CLIENT_ACCESS_TOKEN")


# Search and get lyrics from Genius
def get_lyrics(track_name, track_artist):
    genius = lyricsgenius.Genius(client_access_token)
    song = genius.search_song(track_name, track_artist)
    
    if not song:
        return "Lyrics not found."
    
    lyrics = song.lyrics
    search_phrase = "Lyrics"
    index = lyrics.lower().find(search_phrase.lower())
    
    if index != -1:
        # Get lyrics starting after "Lyrics"
        lyrics = lyrics[index + len(search_phrase):].strip()
    
    # Remove "6Embed" from the end if it is present 
    if lyrics.endswith("6Embed"):
        lyrics = lyrics.rsplit("6Embed", 1)[0].strip()
    
    return lyrics


# Function to split text into chunks of up to 5000 characters due to GoogleTranslator character limit
def split_text(text, max_length=5000):
    lines = text.splitlines()
    batches = []
    current_batch = []

    current_length = 0
    for line in lines:
        line_length = len(line) + 1  # +1 for the newline character
        if current_length + line_length > max_length:
            # If adding this line exceeds the max length, start a new batch
            batches.append("\n".join(current_batch))
            current_batch = [line]
            current_length = line_length
        else:
            current_batch.append(line)
            current_length += line_length
    
    # Add the remaining lines in the final batch
    if current_batch:
        batches.append("\n".join(current_batch))

    return batches



def translate_text(text, target_language):
    try:
        batches = split_text(text)
        translated_batches = []

        for batch in batches:
            translated_batch = GoogleTranslator(source='auto', target=target_language).translate(batch)
            translated_batches.append(translated_batch)

        return "\n".join(translated_batches)
    except Exception as e:
        return f"An error occurred during translation: {str(e)}"
