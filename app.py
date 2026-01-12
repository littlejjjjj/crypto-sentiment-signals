import streamlit as st
import pandas as pd
from sentiment_engine import SentimentEngine

engine = SentimentEngine()
data = engine.analyze()
df = pd.DataFrame(data)

st.title("Crypto Sentiment Signals (MVP)")

# ---- Explanation block ----
st.markdown("""
### 📊 How to Read Sentiment Signals

Scores are normalized from **-1 to +1**:

| Range | Signal |
|---|---|
| **> +0.6** | 🟩 **STRONG BUY** |
| **+0.2 → +0.6** | 🟢 **BUY** |
| **-0.2 → +0.2** | 🟨 **NEUTRAL** |
| **-0.6 → -0.2** | 🔴 **SELL** |
| **< -0.6** | 🟥 **STRONG SELL** |
""")

# ---- Signals feed ----
st.subheader("Latest News Signals")

for row in data:
    title = row['title']
    url = row['url']
    score = row['score']
    signal = row['signal']
    symbol = row['symbol']

    st.markdown(
        f"**[{signal}]** {symbol} ({score:+.2f}) — "
        f"[{title}]({url})",
        unsafe_allow_html=True
    )

# ---- Aggregated chart ----
st.subheader("Sentiment by Symbol")

agg = df.groupby("symbol")["score"].mean().reset_index()
st.bar_chart(agg, x="symbol", y="score")
