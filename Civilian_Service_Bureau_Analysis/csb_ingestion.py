import pandas as pd
import zipfile
import os
import requests
import matplotlib.pyplot as plt

# Define the URL of the zip file
zip_url = 'https://www.stlouis-mo.gov/data/upload/data-files/csb.zip'
zip_file = 'csb.zip'

# Download the zip file and save it to a local file.
response = requests.get(zip_url, allow_redirects=True)
with open(zip_file, 'wb') as f:
    f.write(response.content)

# Extract the zip file and overwrite existing files
# Delete all files in the 'csb_data' directory first
if os.path.exists('csb_data'):
    for file in os.listdir('csb_data'):
        file_path = os.path.join('csb_data', file)
        if os.path.isfile(file_path):
            os.remove(file_path)
else:
    os.makedirs('csb_data')

# Extract the zip file and overwrite existing files
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    for member in zip_ref.namelist():
        zip_ref.extract(member, 'csb_data')

# Read each CSV file and merge them into one DataFrame

# Filter CSV files based on the year in their filenames (e.g., files from 2021 onwards)
csv_files = [f for f in os.listdir('csb_data') if f.endswith('.csv') and int(f[:4]) > 2020]
merged_df_list = []
for csv_file in csv_files:
    print(f"Merging file: {csv_file}")
    df = pd.read_csv(os.path.join('csb_data', csv_file), error_bad_lines=False, encoding='latin1')
    merged_df_list.append(df)
merged_df = pd.concat(merged_df_list)

# Write the merged DataFrame to a new CSV file
merged_csv_file = os.path.join('csb_data', 'merged_csb_data.csv')
merged_df.to_csv(merged_csv_file, index=False)

#delete csb.zip file
os.remove(zip_file)
