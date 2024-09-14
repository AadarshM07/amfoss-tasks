import os
import requests
from imdb import IMDb
from bs4 import BeautifulSoup
import click
import zipfile

BASE_URL = "https://www.opensubtitles.org"  

def extract_imdb_id(input_str):
    """Extract IMDb ID from URL or movie name."""
    movie_name = os.path.splitext(input_str)[0]  # Remove extension if present
    print(f"Searching IMDb for movie: {movie_name}")  # Debugging

    if 'imdb.com/title/' in movie_name:
        imdb_id = movie_name.split('/title/')[1].split('/')[0]
        return imdb_id
    else:
        ia = IMDb()
        search_results = ia.search_movie(movie_name)
        if search_results:
            movie = search_results[0]
            imdb_id = f"tt{movie.movieID}"
            print(f"IMDb ID found: {imdb_id}")  # Debugging
            return imdb_id
        else:
            print(f"No IMDb ID found for movie: {movie_name}")  # Debugging
            return None

def scrape_opensubtitles(imdb_id, language=None, file_size=None):
    """Scrape subtitles from OpenSubtitles with optional file size filter."""
    imdb_id_no_tt = imdb_id[2:]  # Remove 'tt' from IMDb ID
    query = f"{BASE_URL}/en/search/sublanguageid-{language}/imdbid-{imdb_id_no_tt}" if language else f"{BASE_URL}/en/search/idmovie-{imdb_id_no_tt}"
    print(f"Querying OpenSubtitles: {query}")  # Debugging

    response = requests.get(query)
    if response.status_code != 200:
        print(f"Failed to fetch data from OpenSubtitles (Status Code: {response.status_code})")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    subtitles = []

    for subtitle in soup.find_all("tr", class_="even"):
        title_tag = subtitle.find('a', class_='bnone')
        if title_tag:
            subtitle_name = title_tag.text.strip()
            subtitle_url = f"{BASE_URL}{title_tag.get('href')}"
            
            # Check file size filter
            if file_size:
                size_tag = subtitle.find('span', class_='size')
                if size_tag:
                    size_text = size_tag.text.strip()
                    try:
                        size_mb = float(size_text.replace('MB', '').strip())
                        if size_mb > file_size:  # Filter out larger files
                            continue
                    except ValueError:
                        pass  # Ignore size parsing errors

            subtitles.append({
                'title': subtitle_name,
                'download_link': subtitle_url
            })
    
    if not subtitles:
        print("No subtitles found on OpenSubtitles.")  # Debugging
    
    return subtitles

def download_subtitle(download_url, output_dir, filename):
    """Download and extract the .zip subtitle file."""
    download_page = requests.get(download_url)
    soup = BeautifulSoup(download_page.text, "html.parser")
    
    # Extract the actual download link for the .zip file
    download_button = soup.find('a', {'id': 'bt-dwl-bt'})
    if not download_button:
        print("Failed to find the download button on the page.")
        return
    
    zip_link = f"{BASE_URL}{download_button['href']}"
    print(f"Downloading from: {zip_link}")

    # Download the .zip file
    subtitle_response = requests.get(zip_link)
    if subtitle_response.status_code == 200:
        zip_path = os.path.join(output_dir, f"{filename}.zip")
        with open(zip_path, 'wb') as file:
            file.write(subtitle_response.content)
        print(f"Subtitle zip saved as {zip_path}")
        
        # Extract the .zip file
        extract_zip(zip_path, output_dir)
    else:
        print(f"Failed to download the subtitle (Status Code: {subtitle_response.status_code})")

def extract_zip(zip_path, extract_to):
    """Extracts a zip file to the specified directory."""
    if not zipfile.is_zipfile(zip_path):
        print(f"The file {zip_path} is not a valid zip file.")
        return
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Extracted {zip_path} to {extract_to}")


@click.command()
@click.argument('input', type=str)
@click.option('-l', '--language', default='eng', help='Subtitle language (e.g., eng, spa, all).')
@click.option('-o', '--output', default='.', help='Directory to save the subtitle links.')
@click.option('-s', '--size', type=float, default=None, help='Maximum subtitle file size in MB.')
def main(input, language, output, size):
    """Main function to scrape subtitles."""
    base_name = os.path.splitext(os.path.basename(input))[0] if os.path.isfile(input) else input
    imdb_id = extract_imdb_id(input)

    if imdb_id:
        subtitles = scrape_opensubtitles(imdb_id, language, size)
        if subtitles:
            print(f"Found {len(subtitles)} subtitles:")
            for i, subtitle in enumerate(subtitles, 1):
                print(f"{i}. {subtitle['title']}")

            choice = click.prompt("Choose a subtitle by number", type=int, default=1)
            chosen_subtitle = subtitles[choice - 1]
            print(f"Download link: {chosen_subtitle['download_link']}")

            # Proceed to download the subtitle
            download_subtitle(chosen_subtitle['download_link'], output, base_name)
        else:
            print("No subtitles found.")
    else:
        print("Could not find IMDb ID for the movie.")

if __name__ == '__main__':
    main()
