import pandas as pd

class MeanReversionStrategy:
    def __init__(self, lookback=20, entry_z=1.5, exit_z=0.0):
        self.lookback = lookback
        self.entry_z = entry_z
        self.exit_z = exit_z

    def generate_signals(self, df: pd.DataFrame) -> pd.DataFrame:
        prices = df['close']
        mean = prices.rolling(self.lookback).mean()
        std = prices.rolling(self.lookback).std()
        z = (prices - mean) / std
        signals = pd.Series(0, index=df.index)
        signals[z < -self.entry_z] = 1
        signals[z > self.entry_z] = -1
        df['signal'] = signals.ffill().fillna(0)
        return df