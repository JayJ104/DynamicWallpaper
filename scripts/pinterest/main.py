from dataset_functions import *
from pin_link_scraper import *

all_cols = ['id', 'track', 'artist', 'genre', 'year', 'bpm', 'energy', 'danceability', 'loudness', 'liveness', 'valence', 'track_length', 'acousticness', 'speechiness', 'popularity']

def main():
    spotify_2k = load_kaggle_data()

    # querying by year and popularity
    spotify_2k = sql_query(spotify_2k, "SELECT * FROM df WHERE year>=2010 AND popularity>50 ORDER BY popularity DESC")
    write_to_HTML(spotify_2k, "recentSongs.html")
    print(len(spotify_2k))
    spotify_2k.to_csv("../../data/recentSongs.csv")


    # downloading images
    all_search_keys = get_all_search_keys(spotify_2k)
    write_to_txt(all_search_keys, "search_keys.txt")

    all_pin_urls = get_all_pin_urls(all_search_keys)
    write_to_txt(all_pin_urls, "pin_urls.txt")

    if len(all_pin_urls):
        folder = "pins"
        downloaded_files = download(all_pin_urls, folder)
        write_to_txt(downloaded_files, "downloads.txt")

    # add images to spotify2k
    df_w_images = add_images(spotify_2k, downloaded_files)
    df_w_images.to_csv("../../data/dataWImages.csv")


if __name__ == "__main__":
    main()