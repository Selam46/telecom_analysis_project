import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        return pd.read_excel(self.file_path)

if __name__ == "__main__":
    loader = DataLoader("data/Week2_challenge_data_source.xlsx")
    df = loader.load_data()
    print(df.head())
