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
    # Create bucket
    # Create file in bucket
    # assert the path where crated is the same as the one from the function
    # Delete file and bucket
    # Test on not existing file