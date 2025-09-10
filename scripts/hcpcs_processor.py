#hcpcs processor
import pandas as pd
import logging
from pathlib import Path
from utils.common_functions import save_to_formats

# Path to the HCPCS data file
file_path = "input/HCPC2025_OCT_ANWEB_v2.txt"

# Define column specifications based on Professor Hants Repository
colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = [
    "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
]

hcpcs = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)
hcpcs

def clean_hcpcs_data(df):
    # Strip whitespace from all string columns
    hcpcs_cleaned = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # Create a smaller dataframe with only the relevant columns
    hcpcs_cleaned = hcpcs_cleaned[["Code", "Description1"]]

    hcpcs_cleaned['last_updated'] = '2025-09-09'

    # Rename columns to standard names
    hcpcs_cleaned = hcpcs_cleaned.rename(columns={
        "Code": "code",
        "Description1": "description",
        "last_updated": "last_updated"
    })

    return hcpcs_cleaned

hcpcs_cleaned = clean_hcpcs_data(hcpcs)

hcpcs_cleaned