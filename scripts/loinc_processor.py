# Loinc Processor
import pandas as pd
import logging
from pathlib import Path
from utils.common_functions import save_to_formats

# Load the Loinc.csv file
def load_loinc_data(file_path):
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Successfully loaded data from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Error loading data from {file_path}: {e}")
        return pd.DataFrame()

loinc = load_loinc_data('input/loinc.csv')

# Clean and Standardize the data
def clean_loinc_data(df):

    # Create a smaller dataframe with only the relevant columns
    loinc_small = df[['LOINC_NUM', 'LONG_COMMON_NAME', 'CLASS', 'STATUS']]

    # Adds a column for the date updated (last_updated)
    loinc_small['last_updated'] = '2025-09-09'

    # Rename columns to standard names
    loinc_small = loinc_small.rename(columns={
        'LOINC_NUM': 'code',
        'LONG_COMMON_NAME': 'description',
        'CLASS': 'category',
        'STATUS': 'status',
        'last_updated': 'last_updated'
    })

    # Filter to keep only active codes
    loinc_small = loinc_small[loinc_small['status'] == 'ACTIVE']

    return loinc_small

loinc_small = clean_loinc_data(loinc)
loinc_small.count()

# Save the refined data as a csv file
save_to_formats(loinc_small, 'output/loinc_small')