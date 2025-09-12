# Resuasable function to save dataframe in csv format without index
def save_to_formats(df, base_filename):
    # Save as CSV using the correct method for pandas or polars
    if hasattr(df, "to_csv"):
        df.to_csv(f"{base_filename}.csv", index=False)
    elif hasattr(df, "write_csv"):
        df.write_csv(f"{base_filename}.csv")
    else:
        raise TypeError("Unsupported DataFrame type for saving to CSV.")
