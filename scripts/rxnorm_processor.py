import polars as pl
from pathlib import Path
from utils.common_functions import save_to_formats

# Define file path
file_path = Path('input/RXNATOMARCHIVE.RRF')

# Define column names
columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

# Read the RXNATOMARCHIVE.RRF file into a Polars DataFrame
rxnorm_df = pl.read_csv(
        file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)

# Process the dataframe to keep only 'code' and 'str' columns
rxnorm_processed = rxnorm_df[['code', 'str']]

rxnorm_processed = rxnorm_processed.with_columns(
        pl.lit('2025-09-12').alias('last_updated')
)

rxnorm_processed = rxnorm_processed.rename({'str': 'description'})

# Save the processed dataframe to CSV
save_to_formats(rxnorm_processed, 'output/rxnorm_processed')