import logging
import json

from cloud_play.file_finder import file_finder
from google.cloud import storage


# This way of testing is a bit too much.
# But I still don't know how to mock stuff!

LOGGER = logging.getLogger(__name__)

def get_project() -> str:
    LOGGER.info("Retrive project_id")
    with open('tests/my_conf.json', 'r') as f:
        return json.load(f)["project_id"]

def test_file_finder():
    client = storage.Client()

    # Create bucket
    bucket_id = "bucket_test_dan"
    bucket = client.create_bucket(bucket_id)

    # Create file in bucket
    blob_id = "blob_test_dan"
    blob = bucket.blob(blob_id)
    with blob.open("w") as f:
        f.write("Hello world")

    # assert the path where crated is the same as the one from the function
    assert file_finder(blob_id)[0] == f"{bucket_id}/{blob_id}"

    # Delete file and bucket
    bucket.delete()
    
    # Test on not existing file
    assert file_finder(blob_id) == []