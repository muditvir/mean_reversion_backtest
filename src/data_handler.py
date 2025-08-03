import pandas as pd

class DataHandler:
    def __init__(self, data_path):
        self.data_path = data_path

    def load_data(self, symbol: str) -> pd.DataFrame:
        df = pd.read_csv(f"{self.data_path}/{symbol}.csv", parse_dates=['datetime'])
        return df.set_index('datetime')
