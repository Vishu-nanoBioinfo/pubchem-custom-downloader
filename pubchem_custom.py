import os
import requests
import pandas as pd

# Load the CSV file containing specific CID numbers
csv_file_path = 'cid_smiles_list.csv'  # Update with your CSV file path
df = pd.read_csv(csv_file_path)

# Step 1: Fetch Canonical SMILES for CIDs from the CSV file
def get_cid_smiles(cid):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/CanonicalSMILES/TXT"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return None

# Add Canonical SMILES to the DataFrame
df['Canonical_SMILES'] = df['CID'].apply(get_cid_smiles)

# Step 2: Fetch Compound Names using CIDs
def get_compound_name(cid):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/IUPACName/TXT"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return None

# Add a new column to store the compound names
df['Name'] = df['CID'].apply(get_compound_name)

# Optionally save the DataFrame with compound names and SMILES to a new CSV file
output_csv = 'cid_smiles_names_list.csv'
df.to_csv(output_csv, index=False)

# Step 3: Download 3D SDF Files using CIDs and keep a log of failures
output_dir = 'SDF_files'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

log_file_path = 'failed_sdf_downloads.log'
with open(log_file_path, 'w') as log_file:
    log_file.write("Failed SDF Downloads\n")
    log_file.write("=====================\n")

def download_sdf(cid, output_directory, log_file_path):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/SDF?record_type=3d"
    response = requests.get(url)
    if response.status_code == 200:
        sdf_file_path = os.path.join(output_directory, f"{cid}.sdf")
        with open(sdf_file_path, 'wb') as sdf_file:
            sdf_file.write(response.content)
        print(f"Downloaded SDF for CID: {cid}")
    else:
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"CID {cid} - Failed to download\n")
        print(f"Failed to download SDF for CID: {cid}")

# Iterate over the rows in the DataFrame and download SDF files
for index, row in df.iterrows():
    cid = row['CID']
    download_sdf(cid, output_dir, log_file_path)

print("SDF download completed. Check the log file for any failures.")
