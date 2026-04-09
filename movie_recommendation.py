# Task 4: Movie Recommendation System using Cosine Similarity

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset
data = {
    'Movie': ['Avatar', 'Titanic', 'Avengers', 'Iron Man', 'Hulk'],
    'Action': [1, 0, 1, 1, 1],
    'Romance': [0, 1, 0, 0, 0],
    'SciFi': [1, 0, 1, 1, 0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features only
features = df[['Action', 'Romance', 'SciFi']]

# Calculate similarity matrix
similarity = cosine_similarity(features)

# Recommendation function
def recommend(movie_name):
    if movie_name not in df['Movie'].values:
        print("Movie not found in dataset.")
        return

    index = df[df['Movie'] == movie_name].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nRecommendations for {movie_name}:")

    for i in scores[1:4]:
        print(df.iloc[i[0]]['Movie'])

# Test
recommend("Avatar")