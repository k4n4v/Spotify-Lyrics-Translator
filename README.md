# Spotify Lyrics Translator

## Overview
The Spotify Song Lyrics Translator is a web-based application built using Python and Streamlit, which allows users to fetch song lyrics from Spotify and translate them into a language of their choice. This project integrates with the Spotify's API to retrieve song details, Genius API to retrieve song lyrics, and uses GoogleTranslator from deep-translator to handle the translation process.

## Demo
https://github.com/user-attachments/assets/f72e82d6-4738-48fc-94be-31b18be7f373

## Table of Contents
1. [Features](#features)
2. [Technology Stack](#Technology-Stack)
3. [Prerequisites](#Prerequisites)
4. [Setup and Installation](#Setup-and-Installation)
5. [Usage](#Usage)

## Features
- Fetch song lyrics using Spotify song URLs.
- Translate lyrics to multiple languages, including English, Spanish, French, and German (more can be added).
- Display original and translated lyrics side by side for easy comparison.
- User-friendly interface built with Streamlit.

## Technology Stack
- Backend: Python
- Frontend: Streamlit
- APIs:
    - Spotify API (for retrieving song details)
    - Genius API (for retrieving song lyrics)
    - Google Translator (via deep-translator library for translation)

## Prerequisites
Before installing and running the project, make sure you have the following:
- Python (version 3.10 or higher)
- Virtual environment (venv)
- A Genius API Client Access Token (getting started documentation can be found [here](https://docs.genius.com/#/getting-started-h1))
- Spotify API Client ID and Client Secret (getting started documentation can be found [here](https://developer.spotify.com/documentation/web-api))
- pip (python package installer)

## Setup and Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/k4n4v/Spotify-Lyrics-Translator.git
    cd Spotify-Lyrics-Translator
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    # On Windows, use: venv\Scripts\activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file with your Genius API Client Access Token, Spotify Client ID, and Spotify Client Secret:
    ```bash
    SPOTIFY_CLIENT_ID = ""
    SPOTIFY_CLIENT_SECRET = ""
    GENIUS_CLIENT_ACCESS_TOKEN = ""
    ```

## Usage
1. Run the application:
    ```bash
    streamlit run main.py
    ```

2. Open the app:
    - Once the app starts running, it will open a browser window automatically. If not, go to http://localhost:8501 in your browser.

3. Enter a Spotify song URL, select a language from the dropdown to translate to, and hit Translate button!
