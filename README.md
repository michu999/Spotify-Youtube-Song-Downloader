# Spotify YouTube Downloader

The Spotify YouTube Downloader is a Python-based project that seamlessly combines the power of the Spotify API, Pytube, and the youtubesearchpython library to enhance your music experience. With this tool, users can input a Spotify playlist link, allowing the application to extract artist names and song titles as strings. Leveraging the Spotify API, the project dynamically compiles a list of tracks.

## Table of Contents

- [Description](#description)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

The magic begins when the project utilizes the youtubesearchpython library to scour YouTube for the corresponding music videos. Once the search is complete, the downloader component, powered by Pytube, efficiently fetches and downloads the identified songs. This streamlined process ensures that your favorite tracks are readily available for offline enjoyment.

## Key Features

- Seamlessly extracts artist names and song titles from a Spotify playlist link.
- Utilizes the Spotify API to create a dynamic list of tracks.
- Employs the youtubesearchpython library to find corresponding music videos on YouTube.
- Downloads the identified songs using the robust Pytube library.

## Usage

Whether you're compiling a playlist for your next adventure or simply curating your favorite tunes, the Spotify YouTube Downloader simplifies the process, making it a must-have addition to any music enthusiast's toolkit. Unlock the potential of your Spotify playlists by effortlessly transforming them into an accessible offline music collection.

## Installation

To install the Spotify YouTube Downloader and its dependencies, follow these steps:

1. Clone the repository to your local machine:

        git clone https://github.com/your_username/spotify-youtube-downloader.git

2. Navigate to the project directory:

       cd spotify-youtube-downloader

3. Install the required dependencies using pip:

       pip install -r requirements.txt

4. Run the application:

       python main.py

By following these steps, you will have the Spotify YouTube Downloader installed on your local machine along with all necessary dependencies.

## Usage

Upon running the application, you'll be presented with a command-line interface where you can input a Spotify playlist link. The application will then extract artist names and song titles, search for corresponding music videos on YouTube, and download the identified songs using the Pytube library. Enjoy your favorite tracks offline with the Spotify YouTube Downloader!

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. For major changes, please open an issue first to discuss the proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

