from elasticsearch import Elasticsearch
import csv

# Se connecter à Elasticsearch
es = Elasticsearch(hosts=["http://127.0.0.1:9200"])

# Indexer les données dans Elasticsearch pour la table MAIN_ARTIST
with open("./sound_spot_database.csv", "r") as f:
    reader = csv.reader(f)

    for i, line in enumerate(reader):
        document = {
            "track_name": line[8],
            "main_artist_name": line[13]
        }
        es.index(index="songs", document=document)
