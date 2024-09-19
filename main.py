import streamlit as st
from song import get_track
from lyrics import get_lyrics, translate_text

st.title("Spotify Song Lyrics Translator")
song_url = st.text_input("Enter Spotify song URL:")

languages = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
}
selected_language = st.selectbox("Select language to translate to:", list(languages.keys()))

if st.button("Translate"):
    if song_url:
        track_name, track_artist = get_track(song_url)
        lyrics = get_lyrics(track_name, track_artist)
        translated_text = translate_text(lyrics, languages[selected_language])
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.text_area("Original Lyrics", lyrics, height=400)
        with col2:
            st.text_area("Translated Lyrics", translated_text, height=400)

    else:
        st.error("Please enter a valid Spotify song URL.")
