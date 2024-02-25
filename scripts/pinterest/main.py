from dataset_functions import *
from pin_link_scraper import *

def main():
    spotify_2k = load_kaggle_data()

    # downloading images
    all_search_keys = get_all_search_keys(spotify_2k)
    write_to_txt(all_search_keys, "search_keys.txt")

    all_pin_urls = get_all_pin_urls(all_search_keys)
    write_to_txt(all_pin_urls, "pin_urls.txt")

    if len(all_pin_urls):
        folder = "pins"
        downloaded_files = download(all_pin_urls, folder)
        write_to_txt(downloaded_files, "downloads.txt")

    # create training datasets
    # genre_discriminator_data = create_dataframe(spotify_2k, ["id", "genre"])
    # transfer_learning_data = create_dataframe(spotify_2k)


if __name__ == "__main__":
    main()