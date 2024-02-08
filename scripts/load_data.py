# testing data import
import pandas as pd
from pandasql import sqldf
from IPython.display import display, HTML

data2 = pd.read_csv("../data/Spotify-2000.csv")
# print(data2)
df = pd.DataFrame(data2)
df.columns = ['id', 'track', 'artist', 'genre', 'year', 'bpm', 'energy', 'danceability', 'loudness', 'liveness', 'valence', 'track_length', 'acousticness', 'speechiness', 'popularity']
print(df)

# data = sns.load_dataset("../ data/Spotify-2000.csv")
queryDF = lambda query: sqldf(query, globals())
query = "SELECT * FROM df ORDER BY genre ASC, popularity DESC"

queriedDF = queryDF(query)
# display(HTML(queriedDF.to_html()))
html = queriedDF.to_html()
text_file = open("./index.html", "w")
text_file.write(html)
text_file.close()