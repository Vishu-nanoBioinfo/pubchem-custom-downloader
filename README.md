# pubchem-custom-downloader
A Python script that retrieves molecular data (SMILES, compound names) and downloads 3D SDF files from PubChem based on a custom list of Compound IDs (CIDs) provided in a CSV file. It logs failed downloads and outputs a CSV with compound details.

# PubChem Custom Downloader

This Python script allows users to fetch molecular data (SMILES, compound names, and SDF files) from PubChem based on a custom list of Compound IDs (CIDs) provided in a CSV file. It also logs any failed SDF downloads and generates a new CSV with the compound details.

## Features

- Fetches Canonical SMILES and IUPAC names from PubChem for a list of CIDs.
- Downloads 3D SDF files for each CID (logs failed downloads).
- Generates a new CSV with CIDs, SMILES, and compound names.
- Logs failed downloads to a `failed_sdf_downloads.log` file.

## Requirements

- Python 3.x
- `requests` and `pandas` libraries

You can install the required libraries using:

```bash
pip install -r requirements.txt
