from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder
import json


def recommendation(chanson, data, track_table, num_recommendations=5):
    # Decode the JSON string to a Python list
    try:
        decoded_list = json.loads(chanson)
        if not isinstance(decoded_list, list):
            raise ValueError("Decoded object is not a list.")

    except json.JSONDecodeError:
        # Handle the error if it's not a valid JSON
        print("Error: Invalid JSON format.")
        # Continue function or exit, depending on your error handling strategy
    except ValueError as e:
        # Handle other value errors, e.g., decoded object not being a list
        print(f"Error: {e}")

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
    # chanson = "A Keeper"
    recommended_tracks = []

    for song in decoded_list:
        # Find the index of the given song
        track_idx = track_table[track_table['track_name'] == song].index
    
        if not track_idx.empty:
            track_idx = track_idx[0]  # Get the first index if there are multiple matches

            # Get the most similar tracks
            similar_tracks = list(enumerate(cosine_sim[track_idx]))
            similar_tracks = sorted(similar_tracks, key=lambda x: x[1], reverse=True)

            # Extract the top recommended tracks
            
            for i in range(1, num_recommendations + 1):
                similar_track = track_table.iloc[similar_tracks[i][0]]['track_name']
                similarity_score = similar_tracks[i][1]
                recommended_tracks.append({
                    "track_name": similar_track,
                    "similarity_score": similarity_score
                })

            print(recommended_tracks)

        return recommended_tracks
    else:
        return [{'error': 'Track not found'}]
