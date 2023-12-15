import vertexai
from google.cloud import aiplatform
import pymongo
from vertexai.language_models import TextEmbeddingInput, TextEmbeddingModel
import settings
model = TextEmbeddingModel.from_pretrained("textembedding-gecko@001")

def get_text_embedding(text) -> list:
    #Text embedding with a Large Language Model.
    embeddings = model.get_embeddings(text)
    for embedding in embeddings:
        vector = embedding.values
    return vector

if __name__ == "__main__":

    try:
        client = pymongo.MongoClient(settings.URI_STRING)
        print("Connected to MongoDB")
        db = client[settings.DB]
        coll = db[settings.COLLECTION]
        filter = { "plot_embedding" : { "$exists": False},"plot" : { "$exists": True} }
        for doc in coll.find(filter):
          print("Processing document: {}",doc["_id"])
          text_embed = get_text_embedding([doc["plot"]])
          coll.update_one({"_id" : doc["_id"]}, {"$set" : { "plot_embedding" : text_embed}})
    except requests.exceptions.RequestException as err:
        if client:
           client.close()
        print(f"Error: {err}")
