import pandas as pd


class DataAggregator:
    def __init__(self, file_path):
        """
        Initialize the DataAggregator with the path to the dataset.
        :param file_path: Path to the dataset file
        """
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """
        Load the dataset into a pandas DataFrame.
        """
        self.df = pd.read_excel(self.file_path)
        print("Data loaded successfully. Columns in dataset:")
        print(self.df.columns.tolist())

    def clean_data(self):
        """
        Clean the data by checking for missing columns and filling them with default values.
        """
        required_columns = ['TP DL (Bytes)', 'TP UL (Bytes)', 'Dur. (ms)', 'Bearer Id', 'IMSI']
        
        for col in required_columns:
            if col not in self.df.columns:
                print(f"Warning: Missing column '{col}'. Filling with default values.")
                if col in ['TP DL (Bytes)', 'TP UL (Bytes)', 'Dur. (ms)']:
                    self.df[col] = 0  # Default numeric value
                elif col == 'Bearer Id' or col == 'IMSI':
                    self.df[col] = 'Unknown'  # Default string value

    def aggregate_data(self):
        """
        Aggregate the data per user (IMSI) to calculate key metrics.
        :return: Aggregated DataFrame
        """
        self.clean_data()  # Ensure all required columns are present

        # Perform the aggregation
        agg_df = self.df.groupby('IMSI').agg(
            num_sessions=('Bearer Id', 'count'),
            total_duration=('Dur. (ms)', 'sum'),
            total_download=('TP DL (Bytes)', 'sum'),
            total_upload=('TP UL (Bytes)', 'sum'),
        ).reset_index()

        # Calculate total volume as download + upload
        agg_df['total_volume'] = agg_df['total_download'] + agg_df['total_upload']
        
        return agg_df


# Example usage
if __name__ == "__main__":
    # Replace the path with your actual dataset path
    file_path = "data/Week2_challenge_data_source.xlsx"
    
    aggregator = DataAggregator(file_path)
    aggregator.load_data()
    agg_df = aggregator.aggregate_data()
    
    # Save the aggregated data to a new file
    output_path = "data/aggregated_user_data.xlsx"
    agg_df.to_excel(output_path, index=False)
    print(f"Aggregated data saved to {output_path}")
