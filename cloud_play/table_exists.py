import logging

from google.cloud import bigquery
from google.cloud.exceptions import NotFound



LOGGER = logging.getLogger(__name__)

def table_exists(table_id: str) -> bool:
    client = bigquery.Client()
    
    try:
        client.get_table(table_id)
        return True
    except NotFound:
        return False