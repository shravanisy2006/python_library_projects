import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'pandas/anime-dataset.csv')

df = df[['anime_id' , 'Name' , 'Score' , 'Genres' , 'Type' , 'Episodes' , 'Members' ]]

df = df[(df['Score'] != 'UNKNOWN') & (df['Episodes'] != 'UNKNOWN')]

df.to_csv(r'pandas/anime.csv', index=False)

print(df.head(8))

print("\n")

print("=== Shape of the Dataframe ===\n")
print(df.shape)

print("\n")

print("=== Dataframe Info ===\n")
print(df.info())

print("\n")

print("=== Top 10 Rated Anime ===\n")
top_anime = df.sort_values(by = 'Score' , ascending = False).head(10)
print(top_anime[['Name' , 'Score' , 'Genres']])

print("\n")

print("=== Average Score of Anime ===\n")
avg = df['Score'].astype(float).mean().round(2)
print(avg)

print("\n")

print("=== Most common Genre ===\n")
genre_series = df['Genres'].str.split(',').explode()
most_common = genre_series.value_counts().idxmax()
print("Most common genre is: " , most_common)

print("\n")

print("=== Anime type distribution ===\n")
types = df['Type'].value_counts()
print(types)

print("\n")

print("=== Most popular by members ===\n")
popular = df.sort_values(by='Members' , ascending = False).head(5)
print(popular)

print("\n")

print("=== Average number of episodes ===\n")
avg = df['Episodes'].astype(float).mean().round(2)
print(avg)

print("\n")

print("=== Sort genres by score ===\n")
genre_df = df.copy()

genre_df['Genres'] = genre_df['Genres'].str.split(',')

genre_df = genre_df.explode('Genres')

genre_df['Score'] = genre_df['Score'].astype(float)

genre_scores = (
    genre_df.groupby('Genres')['Score']
    .mean()
    .sort_values(ascending=False).round(2)
)
print(genre_scores.head(10))

print("\n")

types.plot(kind='bar')
plt.title("Anime Type Distrubution")
plt.xlabel("Type")
plt.ylabel("Count")
plt.savefig("anime_type_dist.png")

types.plot(kind='bar')
plt.title("Top Genre Chart")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.savefig("anime_type_dist.png")
plt.show()