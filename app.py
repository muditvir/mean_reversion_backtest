import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.strategy import MeanReversionStrategy
from src.backtester import Backtester
from src.metrics import sharpe_ratio

st.title("Intraday Mean Reversion Backtester Dashboard")

# Inputs
symbol_file = st.text_input("CSV file in data folder", "OHLC.csv")
lookback = st.number_input("Lookback Window", 20)
entry_z = st.number_input("Entry Z-score", 1.5)
exit_z = st.number_input("Exit Z-score", 0.0)
cost = st.number_input("Cost per Trade", 0.0002)

if st.button("Run Backtest"):
    df = pd.read_csv(f"data/{symbol_file}", parse_dates=['datetime']).set_index('datetime')

    strategy = MeanReversionStrategy(lookback, entry_z, exit_z)
    backtester = Backtester(strategy, cost_per_trade=cost)
    results = backtester.run_backtest(df)

    st.write(f"Final Equity: {results['equity_curve'].iloc[-1]:.2f}")
    st.write(f"Sharpe Ratio: {sharpe_ratio(results['strategy_returns'].dropna()):.2f}")

    # Equity curve plot
    fig1, ax1 = plt.subplots()
    ax1.plot(results['equity_curve'])
    ax1.set_title('Equity Curve')
    st.pyplot(fig1)

    # Daily PnL bar chart
    results['daily_pnl'] = results['strategy_returns']
    colors = ['g' if x >= 0 else 'r' for x in results['daily_pnl'].fillna(0)]
    fig2, ax2 = plt.subplots()
    ax2.bar(results.index, results['daily_pnl'], color=colors)
    ax2.set_title('Daily PnL Bar Chart')
    st.pyplot(fig2)
