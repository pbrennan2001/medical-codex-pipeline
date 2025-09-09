import pandas as pd

# Load the Loinc.csv file
loinc = pd.read_csv('input/loinc.csv')

# Loinc information
loinc.info()

# Count unique values in the STATUS column
loinc.STATUS.value_counts()

# Shows first row
loinc.iloc[0]

# Show values for LOINC_NUM column (code)
loinc.LOINC_NUM

# Show values for LONG_COMMON_NAME column (description)
loinc.LONG_COMMON_NAME

# Show values for STATUS column (status)
loinc.STATUS

# Show values for CLASS column (category)
loinc.CLASS

# Create a smaller dataframe with only the relevant columns
loinc_small = loinc[['LOINC_NUM', 'LONG_COMMON_NAME', 'CLASS', 'STATUS']]

# Adds a column for the date updated (last_updated)
loinc_small['last_updated'] = '2025-09-09'

loinc_small = loinc_small.rename(columns={
    'LOINC_NUM': 'code',
    'LONG_COMMON_NAME': 'description',
    'CLASS': 'category',
    'STATUS': 'status',
    'last_updated': 'last_updated'
})

# Only keeps active codes
loinc_small = loinc_small[loinc_small['status'] == 'ACTIVE']

# Save the refined data as a csv file
from utils.common_functions import save_to_formats
save_to_formats(loinc_small, 'output/loinc_small')