from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
from data_aggregator import DataAggregator


class PCAReducer:
    def __init__(self, df, n_components=2):
        self.df = df
        self.n_components = n_components
        self.pca = None

    def perform_pca(self):
        """Performs Principal Component Analysis"""
        numeric_data = self.df.select_dtypes(include='number')
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(numeric_data)

        self.pca = PCA(n_components=self.n_components)
        pca_result = self.pca.fit_transform(scaled_data)

        # Add principal components to the dataframe
        for i in range(self.n_components):
            self.df[f"PC{i+1}"] = pca_result[:, i]

        return self.df, self.pca.explained_variance_ratio_

if __name__ == "__main__":
    agg_file = "data/Week2_challenge_data_source.xlsx"
    aggregator = DataAggregator(agg_file)
    df = aggregator.load_data()
    aggregator.clean_data()
    agg_df = aggregator.aggregate_data()

    pca_reducer = PCAReducer(agg_df)
    reduced_df, variance_ratios = pca_reducer.perform_pca()
    print(reduced_df.head())
    print("Explained Variance Ratios:", variance_ratios)
