
def delete_data(collection_name, ids_to_delete):
    status = milvus_client.delete_entity_by_id(collection_name, ids_to_delete)
    return status
