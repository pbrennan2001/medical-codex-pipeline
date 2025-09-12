from os import rename
import polars as pl
import pandas as pd
import time
from utils.common_functions import save_to_formats

# Load NPI data from a CSV file
def load_npi_data(file_path):
    start_time_polars = time.time()
    npi_data = pl.read_csv(file_path)
    end_time_polars = time.time()
    print(f"Polars read_csv time: {end_time_polars - start_time_polars} seconds")
    return npi_data

# Run the function to load NPI data
npi_data = load_npi_data('input/npidata_input.csv')

# Clean the dataframe
def clean_npi_data(npi_clean):
    # Drop rows with null in the NPI column
    npi_clean = npi_clean.drop_nulls(subset=["NPI"])

    # Remove duplicates based on the NPI column (kept crashing)
    # npi_clean = npi_clean.unique(subset=["NPI"])

    return npi_clean

npi_clean = clean_npi_data(npi_data)

npi_clean

# Process NPI data (select specific columns)
def process_npi_data(npi_process):
    
    # Concatenate last, first, middle name into a single column
    npi_process = npi_process.with_columns(
        (pl.concat_str([npi_process["Provider First Name"], npi_process["Provider Last Name (Legal Name)"]], separator=" ")).alias("Provider Full Name")
    )

    npi_process = npi_process[
        'NPI', 'Provider Full Name'
    ]

    npi_process = npi_process.with_columns(
        pl.lit('2025-09-12').alias('last_updated')
    )

    npi_process = npi_process.rename({
    'NPI': 'code',
    'Provider Full Name': 'description'
})

    return npi_process

npi_process = process_npi_data(npi_clean)

npi_process

# Save the processed data to CSV
save_to_formats(npi_process, 'output/npi_processed')