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

print("=== Highest Rated TV Anime ===\n")
highest_rated_tv = df[(df['Type'] == 'TV') & (df['Score'].astype(float).sort_values(ascending=False).head(1))]
print(highest_rated_tv[['Name' , 'Score' , 'Genres']])

print("\n")

print("=== Highest Rated Movie Anime ===\n")
highest_rated_movie = df[(df['Type'] == 'Movie') & (df['Score'].astype(float).sort_values(ascending=False).head(1))]
print(highest_rated_movie[['Name' , 'Score' , 'Genres']])

print("\n")

print("=== Top 10 Anime by Members ===\n")
top_members = df.sort_values(by='Members' , ascending = False).head(10)
print(top_members[['Name' , 'Members' , 'Score']])

print("\n")

print("=== Top 10 Genres by count ===\n")
top_genres = genre_series.value_counts().head(10)
print(top_genres)

print("\n")

types.plot(kind='bar')
plt.title("Anime Type Distribution")
plt.tight_layout()
plt.grid(axis = 'y')
plt.xlabel("Type")
plt.ylabel("Count")
plt.savefig("anime_type_dist.png")
plt.show()

top_genres.plot(kind='bar')
plt.title("Top Genre Chart")
plt.tight_layout()
plt.grid(axis = 'y')
plt.xlabel("Genre")
plt.ylabel("Count")
plt.savefig("top_genres.png")
plt.show()

genre_scores.head(10).plot(kind='barh')

plt.title("Top Genres by Average Score")
plt.xlabel("Average Score")
plt.ylabel("Genre")

plt.grid(axis='x')
plt.tight_layout()

plt.savefig("genre_score_distribution.png")
plt.show()

top_anime_chart = (df.sort_values(by='Score',ascending=False).head(10))
plt.barh(
    top_anime_chart['Name'],
    top_anime_chart['Score'].astype(float)
)
plt.title("Top 10 Rated Anime")
plt.tight_layout()
plt.grid(axis = 'y')
plt.ylabel("Anime Name")
plt.xlabel("Score")
plt.savefig("top_10_rated.png")
plt.show()
