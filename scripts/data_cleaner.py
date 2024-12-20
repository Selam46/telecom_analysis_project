import pandas as pd

class DataCleaner:
    def __init__(self, df):
        self.df = df

    def clean_data(self):
        # Example: Drop irrelevant columns (to be customized based on inspection)
        self.df = self.df.drop(columns=["RTT DL", "RTT UL"], errors="ignore")

        # Handle missing values
        self.df = self.df.fillna(self.df.mean(numeric_only=True))

        # Rename columns for easier understanding (if necessary)
        self.df.rename(columns={"Dur. (ms)": "Duration_ms", "TP DL (Bytes)": "Total_DL_Bytes"}, inplace=True)

        return self.df

# Example usage
if __name__ == "__main__":
    data_path = "data/Week2_challenge_data_source.xlsx"
    df = pd.read_excel(data_path)
    cleaner = DataCleaner(df)
    cleaned_df = cleaner.clean_data()
    print(cleaned_df.head())
