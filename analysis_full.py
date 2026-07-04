"""
Full analysis pipeline: Bitcoin Market Sentiment vs Hyperliquid Trader Performance
Run in order: merge -> insights -> charts
Inputs expected:
 - historical_data.csv  (Hyperliquid trades)
 - fear_greed_index.csv (Fear/Greed Index)
"""
import pandas as pd
import numpy as np

trades = pd.read_csv('/mnt/user-data/uploads/1783183538979_historical_data.csv')
fg = pd.read_csv('/mnt/user-data/uploads/1783183710675_fear_greed_index.csv')

# parse trade date
trades['Timestamp IST'] = pd.to_datetime(trades['Timestamp IST'], format='%d-%m-%Y %H:%M', errors='coerce')
trades['date'] = trades['Timestamp IST'].dt.date

fg['date'] = pd.to_datetime(fg['date']).dt.date

# simplify sentiment into 2 buckets as well as keep 5-class
sentiment_map = {
    'Extreme Fear': 'Fear', 'Fear': 'Fear',
    'Neutral': 'Neutral',
    'Greed': 'Greed', 'Extreme Greed': 'Greed'
}
fg['sentiment_simple'] = fg['classification'].map(sentiment_map)

merged = trades.merge(fg[['date','classification','sentiment_simple']], on='date', how='left')
print("Merged shape:", merged.shape)
print("Unmatched dates:", merged['classification'].isna().sum())
print(merged['date'].min(), merged['date'].max())
print(fg['date'].min(), fg['date'].max())

merged.to_csv('/home/claude/task/merged.csv', index=False)
import pandas as pd
import numpy as np

df = pd.read_csv('merged.csv')
df = df.dropna(subset=['classification'])

order5 = ['Extreme Fear','Fear','Neutral','Greed','Extreme Greed']
order2 = ['Fear','Neutral','Greed']

print("="*70)
print("1. OVERALL TRADE COUNT BY SENTIMENT")
print("="*70)
print(df['classification'].value_counts().reindex(order5))

print("\n"+"="*70)
print("2. AVG CLOSED PnL PER TRADE BY SENTIMENT (5-class)")
print("="*70)
g = df.groupby('classification')['Closed PnL'].agg(['mean','median','sum','count']).reindex(order5)
print(g)

print("\n"+"="*70)
print("3. AVG CLOSED PnL PER TRADE BY SENTIMENT (simple 3-class)")
print("="*70)
g2 = df.groupby('sentiment_simple')['Closed PnL'].agg(['mean','median','sum','count']).reindex(order2)
print(g2)

print("\n"+"="*70)
print("4. WIN RATE (share of trades with PnL > 0) BY SENTIMENT")
print("="*70)
df['is_win'] = df['Closed PnL'] > 0
wr = df.groupby('sentiment_simple')['is_win'].mean().reindex(order2)
print(wr)

print("\n"+"="*70)
print("5. AVG TRADE SIZE (USD) BY SENTIMENT")
print("="*70)
sz = df.groupby('sentiment_simple')['Size USD'].mean().reindex(order2)
print(sz)

print("\n"+"="*70)
print("6. BUY vs SELL SIDE SHARE BY SENTIMENT")
print("="*70)
side = pd.crosstab(df['sentiment_simple'], df['Side'], normalize='index').reindex(order2)
print(side)

print("\n"+"="*70)
print("7. TOP TRADED COINS OVERALL")
print("="*70)
print(df['Coin'].value_counts().head(10))

print("\n"+"="*70)
print("8. PER-ACCOUNT AVG PnL BY SENTIMENT (top 5 most active accounts)")
print("="*70)
top_acc = df['Account'].value_counts().head(5).index
sub = df[df['Account'].isin(top_acc)]
print(sub.groupby(['Account','sentiment_simple'])['Closed PnL'].mean().unstack().reindex(columns=order2))
