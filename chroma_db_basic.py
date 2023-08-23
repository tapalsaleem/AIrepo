import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="saleem_chromadb_collection")

collection.add(
    documents= ["my name is saleem","my name is not saleem"],
    metadatas= [{"source":"name is true"},{"source":"name is false"}],
    ids = ["id1","id2"]
)

results = collection.query(
    query_texts= ['What is my name?'],
    n_results=2
)
print(results)

