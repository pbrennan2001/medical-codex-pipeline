import polars as pl
from pathlib import Path
from utils.common_functions import save_to_formats

# Define the path to the input file
file_path = Path('input/sct2_Description_Full-en.txt')

# Read the CSV file into a Polars DataFrame based on prof. code
snomed_df = pl.read_csv(
    file_path,
    separator='\t',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True,
    dtypes={
        'id': pl.Utf8,
        'effectiveTime': pl.Utf8,
        'active': pl.Int32,
        'moduleId': pl.Utf8,
        'conceptId': pl.Utf8,
        'languageCode': pl.Utf8,
        'typeId': pl.Utf8,
        'term': pl.Utf8,
        'caseSignificanceId': pl.Utf8
    }
)

# Function to clean and refine the SNOMED data
def clean_snomed_data(df):
    # Filter to keep only active descriptions
    snomed_cleaned = df.filter(pl.col('active') == 1)

    # Select relevant columns
    snomed_cleaned = snomed_cleaned.select([
        pl.col('conceptId').alias('code'),
        pl.col('term').alias('description')
    ])

    # Add a last_updated column with a fixed date
    snomed_cleaned = snomed_cleaned.with_columns(
        pl.lit('2025-09-12').alias('last_updated')
    )

    return snomed_cleaned

# Run the cleaning function
snomed_cleaned = clean_snomed_data(snomed_df)

# Save the cleaned DataFrame to various formats
save_to_formats(snomed_cleaned, 'output/snomed_cleaned')
