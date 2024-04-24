import logging

from google.cloud import storage


LOGGER = logging.getLogger(__name__)

def file_finder(file_check: str) -> str:
    LOGGER.info("Starting file")
    pass