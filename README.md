# Bitcoin Market Sentiment vs. Trader Performance



## Objective
Explore the relationship between Bitcoin market sentiment (Fear & Greed Index) and trader performance using historical trading data from Hyperliquid, to uncover patterns useful for smarter trading strategies.

## Data
- **Trader data**: 211,224 trade executions (account, coin, price, size, side, closed PnL, timestamp, etc.)
- **Sentiment data**: Daily Fear & Greed Index classification (Extreme Fear → Extreme Greed), 2018–2025
- Merged by trade date (99.99% match rate)

## Files
| File | Description |
|---|---|
| `analysis_full.py` | Merges datasets and computes all statistics |
| `charts.py` | Generates the 4 charts below |
| `Sentiment_Trading_Analysis.docx` | Full written report with charts & insights |
| `charts/` | PNG chart images |

## Key Findings

**1. Profitability by sentiment** — Extreme Greed periods had the highest avg profit/trade .



**2. Win rate stays flat (~40%) across all sentiment regimes** — sentiment affects the *size* of wins/losses, not how often trades win.



**3. Traders place bigger bets during Fear** — larger risk-taking during fearful/volatile periods.



**4. Most trading activity happens during moderate sentiment (Fear/Greed), not at extremes** — likely due to thinner participation when sentiment peaks.



## Strategic Takeaways
- Extreme Greed = best avg profit per trade → momentum strategies may work well here, with disciplined exits (traders sell more during Greed).
- Fear = larger position sizes → risk controls (leverage caps) may be warranted here.
- Neutral sentiment = weakest performance zone → consider reducing trade frequency.
- Win rate is stable regardless of sentiment → risk/reward management matters more than "picking winners" based on sentiment alone.
- Trader-level responses to sentiment vary significantly — a single blanket rule won't fit every trader.

## How to Run
```bash
pip install pandas matplotlib
python analysis_full.py   # merges data, prints stats, creates merged.csv
python charts.py          # generates charts/ folder
```
