from pin_link_scraper import *
from dataset_functions import *
import pandas as pd

def main():
    # downloading images
    # all_search_keys = {1: "Maroon 5 Memories"}

    # all_pin_urls = get_all_pin_urls(all_search_keys)

    # if len(all_pin_urls):
    #     folder = "test"
    #     downloaded_files = download(all_pin_urls, folder)

    df = load_data("../../data/transferLearningTrainingDataset.csv")

    new_genres = {
        'australian pop': 'pop',
        'electropop': 'electronic',
        'modern rock': 'rock',
        'dance pop': 'pop',
        'neo mellow': 'pop',
        'big room': 'electronic',
        'australian psych': 'indie',
        'dance rock': 'rock',
        'permanent wave': 'rock',
        'indie pop': 'indie',
        'boy band': 'pop',
        'canadian pop': 'pop',
        'garage rock': 'rock',
        'disco': 'pop',
        'folk-pop': 'contemporary',
        'ccm': 'contemporary',
        'electro house': 'electronic',
        'latin': 'pop',
        'british soul': 'r&b',
        'art pop': 'indie',
        'contemporary country': 'country',
        'la pop': 'pop',
        'east coast hip hop': 'hip hop',
        'electro': 'electronic',       
        'irish singer-songwriter': 'rock', 
        'icelandic indie': 'indie',
        'detroit hip hop': 'hip hop',    
        'celtic rock': 'rock',
        'alternative metal': 'rock',
        'mellow gold': 'rock',
        'alternative rock': 'rock',  
        'dutch pop': 'pop',
        'art rock': 'indie',
        'album rock': 'rock',
        'acoustic pop': 'indie',
        'irish pop': 'pop',     
        'australian dance': 'electronic',
        'metropopolis': 'electronic',
        'modern folk rock': 'country', 
        'adult standards': 'pop',
        'barbadian pop': 'pop',
        'british singer-songwriter': 'pop',
        'alternative dance': 'electronic', 
        'edm': 'electronic', 
        'chamber pop': 'indie',
        'stomp and holler': 'rock',
        'dutch indie': 'indie',
        'canadian folk': 'country',      
        'alternative pop rock': 'indie',
        'belgian pop': 'pop',
        'gabba': 'electronic',
        'glam rock': 'rock',
        'british invasion': 'pop',
        'classic soundtrack': 'contemporary',
        'dutch metal': 'rock'
    }

    df['genre'] = df['genre'].replace(new_genres)
    unique = df['genre'].nunique()
    print(unique)
    df.to_csv("../../data/transferLearningTrainingDataset.csv")



if __name__ == "__main__":
    main()