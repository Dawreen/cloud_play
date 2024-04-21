import logging
import json

from cloud_play.table_exists import table_exists
from google.cloud import bigquery
from google.api_core.exceptions import Conflict


# This way of testing is a bit too much.
# But I still don't know how to mock stuff!

LOGGER = logging.getLogger(__name__)

def get_project() -> str:
    LOGGER.info("Retrive project_id")
    with open('tests/my_conf.json', 'r') as f:
        return json.load(f)["project_id"]

def test_table_finder():
    project_id = get_project() # Can't create project
    
    client = bigquery.Client()

    LOGGER.info("Creating test dataset...")
    # Create test dataset
    dataset_name = "test_dataset"
    dataset_id = f"{project_id}.{dataset_name}"
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "EU"
    try:
        dataset = client.create_dataset(dataset, timeout=30)
    except Conflict:
        LOGGER.error("dataset already exists!")
    LOGGER.info("Test dataset was created!")

    LOGGER.info("Creating test table...")
    #Create test table
    table_name = "test_table"

    # Creating a table
    schema = [
        bigquery.SchemaField("string_field", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("int_field", "INTEGER", mode="REQUIRED"),
    ]
    table_id = f"{project_id}.{dataset_name}.{table_name}"
    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)  # Make an API request.
    LOGGER.info("Created table!")

    LOGGER.info(f"table check: {table_exists(table_id)}")
    assert table_exists(table_id)

    LOGGER.info("Cleaning...")
    # Cleaning
    # Delete dataset and table
    client.delete_dataset(
        dataset_id, delete_contents=True, not_found_ok=True
    )  # Make an API request.
    LOGGER.info("Cleaning done!")