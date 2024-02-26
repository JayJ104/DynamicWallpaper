import pandas as pd
import json
import sys
sys.path.append('./pinterest')
from dataset_functions import *

all_cols = ['id', 'track', 'artist', 'genre', 'year', 'bpm', 'energy', 'danceability', 'loudness', 'liveness', 'valence', 'track_length', 'acousticness', 'speechiness', 'popularity']

def main():
    df = load_data("../data/dataWImages.csv")

    # check if less than 10 images
    with open("pinterest/data/downloads.txt") as f:
        downloads = f.read()

    downloaded_images_dict = json.loads(downloads)
    not_enough_images = []
    for key in downloaded_images_dict:
        if len(downloaded_images_dict[key]) < 10:
            not_enough_images.append(int(key))

    # drop them rows
    new_df = df[~df['id'].isin(not_enough_images)]
    new_df.to_csv("../data/10plusDF.csv")

    # create training datasets
    genre_discriminator_data = create_dataframe("discriminatorTrainingDataset", new_df, ["genre", "image"])
    print(len(genre_discriminator_data))
    transfer_learning_data = create_dataframe("transferLearningTrainingDataset", new_df,['track', 'genre', 'year', 'bpm', 'energy', 'danceability', 'loudness', 'liveness', 'valence', 'track_length', 'acousticness', 'speechiness', 'popularity', 'image'] )
    print(len(transfer_learning_data))


if __name__ == "__main__":
    main()