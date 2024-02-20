import pandas as pd
from pandasql import sqldf

all_cols = ['id', 'track', 'artist', 'genre', 'year', 'bpm', 'energy', 'danceability', 'loudness', 'liveness', 'valence', 'track_length', 'acousticness', 'speechiness', 'popularity']

def load_kaggle_data():
    data = pd.read_csv("../../data/Spotify-2000.csv")
    df = pd.DataFrame(data)
    df.columns = all_cols
    return df

def load_data(csvfilepath: str):
    data = pd.read_csv(csvfilepath)
    df = pd.DataFrame(data)
    return df

def sql_query(df: pd.DataFrame, query: str) -> pd.DataFrame:
    queryDF = lambda query: sqldf(query, {'df': df})
    queriedDF = queryDF(query)
    print('Querying...')
    return queriedDF

def write_to_HTML(df: pd.DataFrame, file: str):
    html = df.to_html()
    print('Writing to file...')
    file = "../../data/" + file
    text_file = open(file, "w")
    text_file.write(html)
    text_file.close()
    print('Dataframe written to file', file)

def create_dataframe(df: pd.DataFrame, cols_list=all_cols):
    # copy kaggle dataset's subdataset
    # add images
    df = add_images(df)
    # export as csv
    return #dataframe

def add_images(df: pd.DataFrame):
    # add image path lists to each row
    # explode by images col
    return #dataframe

def get_all_search_keys():
    
    return # search_keys