import logging

from google.cloud import storage


LOGGER = logging.getLogger(__name__)

def file_finder(file_name: str) -> list[str]:
    LOGGER.info("Starting file_finder")
    
    client = storage.Client("")

    all_buckets = client.list_buckets()
    ret = []
    for bucket in all_buckets:
        all_blobs = client.list_blobs(bucket)
        for blob in all_blobs:
            if file_name == blob.name:
                LOGGER.info(f"path: {blob.path}")
                ret.append(blob.path)
    return ret