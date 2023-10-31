from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from elasticsearch import Elasticsearch
import song_rec
import pandas as pd

data = pd.read_csv('sound_spot_database.csv', delimiter=',')
track_table = pd.read_csv('track_table.csv', delimiter=',')



es = Elasticsearch(hosts=["http://127.0.0.1:9200"])
print(f"Connected to ElasticSearch cluster `{es.info().body['cluster_name']}`")

app = Flask(__name__)

cors_config = {
    "origins": ["http://localhost:5000"],
    "methods": ["OPTIONS", "GET", "POST"],
    "allow_headers": ["Authorization"]
}


CORS(app, resources={
    r"/*": cors_config,
})

MAX_SIZE = 15

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results")
def results():
    chansons_selectionnees = request.args.get('chansons')
    chansons_selectionnees2 = song_rec.recommendation(chansons_selectionnees, data, track_table)
    return render_template("results.html", chansons_selectionnees=chansons_selectionnees2)

@app.route("/search")
def search_autocomplete():
    query = request.args["q"].lower()
    tokens = query.split(" ")

    clauses_track = [
        {
            "span_multi": {
                "match": {"fuzzy": {"track_name": {"value": i, "fuzziness": "AUTO"}}}
            }
        }
        for i in tokens
    ]


    payload_track = {
        "bool": {
            "must": [{"span_near": {"clauses": clauses_track, "slop": 0, "in_order": False}}]
        }
    }

    # resp_main_artist = es.search(index="MAIN_ARTIST", query=payload_main_artist, size=MAX_SIZE)
    resp_track = es.search(index="songs", query=payload_track, size=MAX_SIZE)

    # Fusionner les résultats des deux recherches
    combined_results = [result['_source']['track_name'] for result in resp_track['hits']['hits']]

    # Supprimer les doublons
    combined_results = list(set(combined_results))

    # Activer CORS en ajoutant les en-têtes appropriés
    response = jsonify(combined_results)
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5000/')  # Ajustez l'origine au besoin

    return response



if __name__ == "__main__":
    app.run(debug=True)

