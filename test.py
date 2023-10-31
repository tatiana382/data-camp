from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder

def hello():
    return("hello")

def ese(chanson):
    return(chanson)



def recommendation(chanson, data, track_table, num_recommendations=5):
    # Create a LabelEncoder instance
    label_encoder = LabelEncoder()

    columns_to_encode = ['track_name', 'other_artists', 'lyrics', 'main_artist_name', 'main_artist_genre']

    for col in columns_to_encode:
        data[col] = label_encoder.fit_transform(data[col])

    # Calculate cosine similarity between tracks based on selected features
    features = ['loudness', 'track_popularity', 'track_name',
                'track_popularity', 'other_artists', 'lyrics',
                'main_artist_name', 'main_artist_popularity',
                'main_artist_genre']

    data_features = data[features].fillna(0)
    cosine_sim = cosine_similarity(data_features)

    # Find the index of the given song
    track_idx = track_table[track_table['track_name'] == chanson].index

    if not track_idx.empty:
        track_idx = track_idx[0]  # Get the first index if there are multiple matches

        # Get the most similar tracks
        similar_tracks = list(enumerate(cosine_sim[track_idx]))
        similar_tracks = sorted(similar_tracks, key=lambda x: x[1], reverse=True)

        # Extract the top recommended tracks
        recommended_tracks = []
        for i in range(1, num_recommendations + 1):
            similar_track = track_table.iloc[similar_tracks[i][0]]['track_name']
            similarity_score = similar_tracks[i][1]
            recommended_tracks.append({
                "track_name": similar_track,
                "similarity_score": similarity_score
            })

        return recommended_tracks
    else:
        return []

# Example usage:
# recommended_tracks = recommendation("Mourning", data, track_table)
# print(recommended_tracks)


# def recommendation(chanson):

#     # Create a LabelEncoder instance
#     label_encoder = LabelEncoder()

#     columns_to_encode = ['track_name', 'other_artists', 'lyrics', 'main_artist_name', 'main_artist_genre']

#     for col in columns_to_encode:
#         data[col] = label_encoder.fit_transform(data[col])

#     from sklearn.metrics.pairwise import cosine_similarity

#     # Calculate cosine similarity between tracks based on selected features
#     features = ['loudness', 'track_popularity', 'track_name',
#                 'track_popularity', 'other_artists', 'lyrics',
#                 'main_artist_name', 'main_artist_popularity',
#                 'main_artist_genre']

#     data_features = data[features].fillna(0)
#     cosine_sim = cosine_similarity(data_features)

#     # Get recommendations for a specific track
#     track_name = "Mourning"
#     track_idx = track_table[track_table['track_name'] == track_name].index[0]

#     # Get the most similar tracks
#     similar_tracks = list(enumerate(cosine_sim[track_idx]))
#     similar_tracks = sorted(similar_tracks, key=lambda x: x[1], reverse=True)

#     # Print the top recommended tracks
#     num_recommendations = 5
#     for i in range(1, num_recommendations + 1):
#         similar_track = track_table.iloc[similar_tracks[i][0]]['track_name']
#         similarity_score = similar_tracks[i][1]  # Score de similarité
#         print(f"Recommendation {i}: {similar_track} (Similarity Score: {similarity_score})")
