import pandas as pd
from pandasql import sqldf

def load_kaggle_data():
    data = pd.read_csv("../data/Spotify-2000.csv")
    df = pd.DataFrame(data)
    df.columns = ['id', 'track', 'artist', 'genre', 'year', 'bpm', 'energy', 'danceability', 'loudness', 'liveness', 'valence', 'track_length', 'acousticness', 'speechiness', 'popularity']
    return df

def sql_query(df: pd.DataFrame, query: str) -> pd.DataFrame:
    queryDF = lambda query: sqldf(query, {'df': df})
    queriedDF = queryDF(query)
    print('Querying...')
    return queriedDF

def write_to_HTML(df: pd.DataFrame, file: str):
    html = df.to_html()
    print('Writing to file...')
    text_file = open(file, "w")
    text_file.write(html)
    text_file.close()
    print('Dataframe written to file', file)
