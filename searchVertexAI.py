from vertexai.preview.language_models import TextEmbeddingModel
import pymongo
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
        print(settings.COLLECTION)
        print("Enter the text to search:")
        input_text = input()
        input_vector = get_text_embedding([input_text])
           # Query for similar documents.
        results = list(
            coll.aggregate(
                [
                    {
                        "$vectorSearch": {
                            "index":"default",
                            "queryVector": input_vector,
                            "path": "plot_embedding",
                            "numCandidates": 20,
                            "limit":5
                            },
                        },
                    {"$project": {"_id": 0, "plot": 1, "title": 1}},
                ]
            )
        )
        for doc in results:
            print(str(doc) + "\n")
    except Exception:
        traceback.print_exc()

    finally:
        client.close()
