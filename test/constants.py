from datetime import timedelta

PROJECT_ID = 'bigquery-devrel-samples'
DATASET_ID = 'test_dataset'
CURRENT_TABLE_ID = 'test_table'
NEW_TABLE_ID = 'test_table2'
GCS_INPUT_URI = 'gs://bigquery-devrel-samples-bucket/data.csv'
GCS_OUTPUT_URI = 'gs://bigquery-devrel-samples-bucket/output.csv'
QUERY = 'SELECT corpus FROM publicdata:samples.shakespeare GROUP BY corpus;'
SCHEMA_PATH = './test/data/schema.json'
DATA_PATH = './test/data/data.csv'
DISCOVERY_DOC_MAX_AGE = timedelta(hours=24).seconds
DISCOVERY_DOC_PATH = './test/data/'
