# Song Blog Generator

This web application allows users to generate blog posts about songs. Users can input the name of a song, and the application retrieves song information from Spotify, lyrics from Genius, and generates a blog post using OpenAI's GPT-3.5 model.

## Features

- **Song Information Retrieval:** Utilizes the Spotify API to retrieve song information such as artist, album, and audio features.
- **Lyrics Retrieval:** Utilizes the Genius API to retrieve the lyrics of the specified song.
- **Blog Post Generation:** Uses OpenAI's GPT-3.5 model to generate a blog post about the song based on retrieved information.
- **Web Interface:** Provides a user-friendly web interface for users to input song names and view generated blog posts.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/potternate/openai-spotify-genius.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    Create a `.env` file in the root directory and add the following environment variables:

    ```plaintext
    SPOTIFY_CLIENT_ID=your_spotify_client_id
    SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
    GENIUS_API_KEY=your_genius_api_key
    OPENAI_API_KEY=your_openai_api_key
    ```

4. Run the application:

    ```bash
    python app.py
    ```

## Usage

1. Access the web interface by navigating to `http://localhost:5000` in your web browser.

2. Enter the name of the song you want to generate a blog post about and submit the form.

3. View the generated blog post on the webpage.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
