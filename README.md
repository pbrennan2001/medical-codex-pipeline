# medical-codex-pipeline

## Overview
This repository contains codes to take raw data for different medical codexes and transforms them into a standardized CSV format.

## Before Using the Codes
Ensure all raw codex files are saved into the input folder. To obtain data, follow the links below:

- **Snowmed (US):** https://www.nlm.nih.gov/healthit/snomedct/archive.html

- **ICD-10-CM (US):** https://www.cms.gov/medicare/coding-billing/icd-10-codes 

- **ICD-10 (WHO):** https://icdcdn.who.int/icd10/index.html 

- **HCPCS (US):** https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system/quarterly-update 

- **LOINC (US):** https://loinc.org/downloads/ 

- **RxNorm (US):** https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html 

- **NPI (US) :** https://download.cms.gov/nppes/NPI_Files.html 

## Usage
Before using each program, ensure all required modules are properly installed and imported. For example:
```python
import pandas as pd
import logging
from pathlib import Path
from utils.common_functions import save_to_formats
```
All required modules are included in the requirements.txt, and listed at the top of each processor.

### Program Structure
For each of the processors, the code can be broken down into loading and cleaning the data.

#### Loinc Example
Loading Data: 
```python
def load_loinc_data(file_path):
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Successfully loaded data from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Error loading data from {file_path}: {e}")
        return pd.DataFrame()

loinc = load_loinc_data('input/loinc.csv')
```
*Note that the file you save in the input folder for loinc must follow the path 'input/loinc.csv'

Cleaning Data:
```python
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
```

### Exporting to CSV
Finally, each program uses the common function "save_to_formats"
```python
save_to_formats(loinc_small, 'output/loinc_small')
```
