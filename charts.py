import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.read_csv('merged.csv')
df = df.dropna(subset=['classification'])
order5 = ['Extreme Fear','Fear','Neutral','Greed','Extreme Greed']
order2 = ['Fear','Neutral','Greed']

plt.style.use('seaborn-v0_8-whitegrid')

# Chart 1: Avg PnL by 5-class sentiment
g = df.groupby('classification')['Closed PnL'].mean().reindex(order5)
fig, ax = plt.subplots(figsize=(8,5))
colors = ['#b91c1c','#f87171','#9ca3af','#4ade80','#15803d']
ax.bar(g.index, g.values, color=colors)
ax.set_title('Average Closed PnL per Trade by Market Sentiment')
ax.set_ylabel('Avg Closed PnL (USD)')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('charts/avg_pnl_by_sentiment.png', dpi=150)
plt.close()

# Chart 2: Win rate by simple sentiment
wr = df.assign(is_win=df['Closed PnL']>0).groupby('sentiment_simple')['is_win'].mean().reindex(order2)
fig, ax = plt.subplots(figsize=(6,5))
ax.bar(wr.index, wr.values*100, color=['#f87171','#9ca3af','#4ade80'])
ax.set_title('Win Rate (%) by Market Sentiment')
ax.set_ylabel('Win Rate %')
plt.tight_layout()
plt.savefig('charts/winrate_by_sentiment.png', dpi=150)
plt.close()

# Chart 3: Avg trade size by sentiment
sz = df.groupby('sentiment_simple')['Size USD'].mean().reindex(order2)
fig, ax = plt.subplots(figsize=(6,5))
ax.bar(sz.index, sz.values, color=['#f87171','#9ca3af','#4ade80'])
ax.set_title('Average Trade Size (USD) by Market Sentiment')
ax.set_ylabel('Avg Size (USD)')
plt.tight_layout()
plt.savefig('charts/avgsize_by_sentiment.png', dpi=150)
plt.close()

# Chart 4: trade volume count by sentiment
cnt = df['classification'].value_counts().reindex(order5)
fig, ax = plt.subplots(figsize=(8,5))
ax.bar(cnt.index, cnt.values, color=colors)
ax.set_title('Number of Trades by Market Sentiment')
ax.set_ylabel('Trade Count')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('charts/tradecount_by_sentiment.png', dpi=150)
plt.close()

print("done")
