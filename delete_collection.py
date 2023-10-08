
def delete_collection(collection_name):
    status = milvus_client.drop_collection(collection_name)
    return status
