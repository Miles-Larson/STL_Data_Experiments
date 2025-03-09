from google.cloud import bigquery
import pandas as pd

# Initialize a BigQuery client
client = bigquery.Client(project='dedicated-server-hosting')

# Define the BigQuery dataset and table
dataset_id = 'CSB'
table_id = 'csb'
table_ref = client.dataset(dataset_id).table(table_id)

# Load the CSV data into a DataFrame
csv_file_path = 'csb_data\merged_csb_data.csv'
df = pd.read_csv(csv_file_path)

# Convert DataFrame to BigQuery table
job = client.load_table_from_dataframe(df, table_ref)

# Wait for the job to complete
job.result()

print(f"Loaded {job.output_rows} rows into {dataset_id}:{table_id}.")