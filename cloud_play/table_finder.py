import logging

from google.cloud import bigquery



LOGGER = logging.getLogger(__name__)

def table_finder(table_id: str):
    client = bigquery.CLient()
    table = client.get_table(table_id)
    return table

# # View table properties
# print(
#     "Got table '{}.{}.{}'.".format(table.project, table.dataset_id, table.table_id)
# )
# print("Table schema: {}".format(table.schema))
# print("Table description: {}".format(table.description))
# print("Table has {} rows".format(table.num_rows))