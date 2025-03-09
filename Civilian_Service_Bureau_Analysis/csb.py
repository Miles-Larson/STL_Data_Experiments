import pandas as pd
import zipfile
import os
import requests
import matplotlib.pyplot as plt

# Define the URL of the zip file
zip_url = 'https://www.stlouis-mo.gov/data/upload/data-files/csb.zip'
zip_file = 'csb.zip'

# Download the zip file
zip_file = requests.get(zip_url, allow_redirects=True).content

# Extract the zip file
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall('csb_data')

# Read each CSV file and merge them into one DataFrame
csv_files = [f for f in os.listdir('csb_data') if f.endswith('.csv')]
merged_df = pd.concat([pd.read_csv(os.path.join('csb_data', csv_file)) for csv_file in csv_files])

# Write the merged DataFrame to a new CSV file
merged_csv_file = 'merged_csb_data.csv'
merged_df.to_csv(merged_csv_file, index=False)

# Build visualizations from the merged CSV
# Example: Plotting the first two columns
merged_df.plot(kind='bar', x=merged_df.columns[0], y=merged_df.columns[1])
plt.show()