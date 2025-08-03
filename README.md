# Mean Reversion Backtester

A Python-based research framework for backtesting intraday **mean-reversion trading strategies** on OHLC futures data — now with both **CLI script** and **interactive Streamlit dashboard**.

---

## ⚙️ Installation

```bash
git clone <repo-url>
cd mean_reversion_backtest
pip install -r requirements.txt
```

---

## ▶️ Run from Command Line

```bash
python main.py
```

- Loads `data/OHLC.csv`
- Runs mean reversion strategy (lookback=20, entry\_z=1.5)
- Shows *equity curve* and *daily PnL chart*
- Saves results to:
  - `results/pnl_curve.png`
  - `results/pnl_series.csv`

---

## 📊 Strategy Logic

Mean reversion based on **Z-score of closing price**:

| Condition           | Action |
| ------------------- | ------ |
| z-score < −entry\_z | Long   |
| z-score > +entry\_z | Short  |
| within exit\_z      | Flat   |

Default parameters:

```python
lookback = 20
entry_z  = 1.5
exit_z   = 0.0
cost     = 0.0002
```

---

## 🖥️ Interactive Dashboard

Launch Streamlit interface:

```bash
streamlit run app.py
```

Features:

- Upload/select CSV file from *data/*
- Change Z-score thresholds & cost
- View:
  - **Equity curve line plot**
  - **Daily PnL colored bar chart** (green → profit, red → loss)

---

