
from pymilvus import Milvus, DataType

milvus_client = Milvus(host='your_host', port='your_port')

def create_collection(collection_name, dimension):
    collection_schema = {
        "fields": [
            {"name": "embedding", "type": DataType.FLOAT_VECTOR, "params": {"dim": dimension}}
        ],
        "segment_row_limit": 10000,
        "auto_id": True
    }
    status = milvus_client.create_collection(collection_name, collection_schema)
    return status
