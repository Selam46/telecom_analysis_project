import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from data_aggregator import DataAggregator


class EDAVisualizer:
    def __init__(self, df):
        self.df = df

    def describe_data(self):
        """Describes relevant variables and their statistics"""
        return self.df.describe()

    def univariate_analysis(self):
        """Plots distribution for key variables"""
        numeric_cols = self.df.select_dtypes(include='number').columns
        for col in numeric_cols:
            plt.figure(figsize=(8, 5))
            sns.histplot(self.df[col], kde=True, bins=30)
            plt.title(f"Distribution of {col}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.show()

    def bivariate_analysis(self):
        """Explores relationships between variables"""
        sns.pairplot(self.df, diag_kind='kde')
        plt.show()

    def correlation_analysis(self):
        """Computes and visualizes correlation matrix"""
        corr_matrix = self.df.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title("Correlation Matrix")
        plt.show()

if __name__ == "__main__":
    # Example usage
    agg_file = "data/Week2_challenge_data_source.xlsx"
    aggregator = DataAggregator(agg_file)
    df = aggregator.load_data()
    aggregator.clean_data()
    agg_df = aggregator.aggregate_data()

    eda = EDAVisualizer(agg_df)
    print(eda.describe_data())
    eda.univariate_analysis()
    eda.correlation_analysis()
