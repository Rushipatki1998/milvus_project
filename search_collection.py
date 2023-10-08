
def search_collection(collection_name, query_embeddings, top_k):
    search_params = {"metric_type": "L2"}
    status, results = milvus_client.search(collection_name, top_k, query_embeddings, params=search_params)
    return status, results
