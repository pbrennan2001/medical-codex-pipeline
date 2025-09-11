# icd10cm_processor.py
import pandas as pd
import logging
from pathlib import Path
from utils.common_functions import save_to_formats

# Define file path
file_path = "input/icd10cm_order_2025.txt"



# Create a DataFrame from the parsed codes
icdcodes = pd.DataFrame(codes)

# Save the DataFrame to CSV format using the reusable function
save_to_formats(icdcodes, 'output/icd10cm_2025_codes')