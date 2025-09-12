# icd10who_processor.py
import pandas as pd
from utils.common_functions import save_to_formats

# Define the column names as per the ICD-10-WHO documentation
columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

# Function to load the ICD-10-WHO data
def load_icd10who_data(file_path):
    
    icd10_who_codes = pd.read_csv(file_path, sep=';', header=None, names=columns)
    return icd10_who_codes

# Load the data
icd10who_codes = load_icd10who_data('input/icd102019syst_codes.txt')

# Display basic information about the dataframe
icd10who_codes.info()

icd10who_codes.title_en

# Clean and refine the Data
def clean_icd10who_data(df):
    # Create a smaller dataframe with only the relevant columns
    icd10who_small = df[['code', 'title_en']]

    # Adds a column for the date updated (last_updated)
    icd10who_small['last_updated'] = '2025-09-12'

    # Rename columns to standard names
    icd10who_small = icd10who_small.rename(columns={
        'title_en': 'description',
    })

    return icd10who_small

icd10who_small = clean_icd10who_data(icd10who_codes)

save_to_formats(icd10who_small, 'output/icd10who_codes')