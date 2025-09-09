
# Resuasable function to save dataframe in csv format without index
def save_to_formats(df, base_filename):
    df.to_csv(f'{base_filename}.csv', index=False)