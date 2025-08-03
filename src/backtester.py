import pandas as pd

class Backtester:
    def __init__(self, strategy, cost_per_trade=0.0002):
        self.strategy = strategy
        self.cost_per_trade = cost_per_trade

    def run_backtest(self, df: pd.DataFrame):
        df = self.strategy.generate_signals(df)
        df['returns'] = df['close'].pct_change()
        df['strategy_returns'] = df['returns'] * df['signal'].shift(1)
        df['strategy_returns'] -= self.cost_per_trade * df['signal'].diff().abs()
        df['equity_curve'] = (1 + df['strategy_returns']).cumprod()
        return df
