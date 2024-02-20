from dataset_functions import *
from pin_link_scraper import *

def main():
    spotify_2k = load_kaggle_data()

    # downloading images
    all_search_keys = get_all_search_keys()
    print(all_search_keys)


    all_pin_urls = get_all_pins_url(all_search_keys)
    all_pin_urls = get_all_pin_urls({1: "the beatles here comes the sun"})
    print(all_pin_urls)

    if len(all_pin_urls):
        for key in all_pin_urls:
            folder = "./pins/" + str(key) + "/"
            try:
                download(all_pin_urls[key], folder)
            except KeyboardInterrupt:
                print("Could not download images for key", key)

    # download_this_image()

    # create training datasets
    # genre_discriminator_data = create_dataframe(spotify_2k, ["id", "genre"])
    # transfer_learning_data = create_dataframe(spotify_2k)


if __name__ == "__main__":
    main()