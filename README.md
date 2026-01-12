# Crypto Sentiment Signals

AI-powered crypto sentiment dashboard that ingests real crypto news feeds, applies transformer-based sentiment scoring, and generates actionable BUY/SELL style sentiment signals for major digital assets. Runs 100% locally with no API billing or external dependencies.

---

## 🎯 Project Overview

This MVP demonstrates a practical use of NLP in crypto markets:

- Collects crypto news via RSS feeds
- Performs sentiment classification using a local transformer model
- Maps headlines to symbols (BTC / ETH / SOL / etc.)
- Generates trading-style sentiment signals
- Displays results via a Streamlit dashboard

This offers a fast, low-noise signal surface for traders, analysts, and researchers.

---

## 🧠 Sentiment Model

The system uses:

```
distilbert-base-uncased-finetuned-sst-2-english
```

A lightweight transformer from HuggingFace optimized for binary sentiment analysis (positive/negative). Output is normalized to:

```
+1.00 → Strong Bullish
 0.00 → Neutral
-1.00 → Strong Bearish
```

---

## 📊 How to Read Sentiment Signals

| Score Range | Signal | Meaning |
|---|---|---|
| **> +0.60** | 🟩 **STRONG BUY** | very bullish catalyst |
| **+0.20 → +0.60** | 🟢 **BUY** | bullish optimism |
| **-0.20 → +0.20** | 🟨 **NEUTRAL** | mixed / no direction |
| **-0.60 → -0.20** | 🔴 **SELL** | bearish pressure |
| **< -0.60** | 🟥 **STRONG SELL** | negative catalyst / fear |

These are sentiment interpretations, not financial recommendations.

---

## 🗂 Current Data Sources (MVP)

Data Input:
- Crypto News RSS (CoinTelegraph, CoinDesk)

Signals:
- Sentiment model
- Symbol mapping (BTC / ETH / SOL / GENERAL)

UI:
- Streamlit dashboard
- Clickable headlines
- Symbol aggregation chart

No API keys required.

---

## 🏗 Project Structure

```
crypto-sentiment-signals/
├── app.py
├── sentiment_engine.py
├── models/
│   └── sentiment_model.py
├── sources/
│   └── news.py
├── data/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📦 Installation

Requires Python 3.10+

```bash
git clone https://github.com/littlejjjjj/crypto-sentiment-signals
cd crypto-sentiment-signals
pip install -r requirements.txt
```

The first run will download model weights from HuggingFace automatically.

---

## ▶️ Running the Dashboard

```bash
streamlit run app.py
```

Then open the UI in your browser (default):

```
http://localhost:8501
```

---

## 🖥 Example Output

Example sentiment feed:

```
[SELL] BTC (-0.41) — SEC delays spot ETF approval again 🔗
[STRONG BUY] ETH (+0.74) — BlackRock ETF demand surges 🔗
[NEUTRAL] GENERAL (+0.05) — New exchange expands crypto access 🔗
```

Aggregated symbol scores:

```
BTC: -0.41
ETH: +0.74
GENERAL: +0.05
```

---

## 🛣 Roadmap

**v0.2 — Data Expansion**
- Reddit sentiment
- Twitter/X sentiment
- Weighted source scoring

**v0.3 — Price Correlation**
- Binance price feed
- Price + sentiment divergence detection

**v0.4 — Alerts**
- Telegram/Discord/Slack/Email
- Real-time signal pushes

**v0.5 — Persistence**
- SQLite/Postgres
- Historical sentiment visualization

**v1.0 — Research Mode**
- Export dataset for quant analysis
- Backtesting hooks

---

## 🧑‍💻 Maintainer

**Jovian Tan (littlejjjjj)**  
Email: `jovian.t@outlook.com`  
GitHub: `https://github.com/littlejjjjj`  
LinkedIn: `https://www.linkedin.com/in/joviantan/`

---

## 📜 License

MIT License

---

## ⚠️ Disclaimer

This project performs sentiment analysis.  
It does **not** provide financial advice or trading recommendations.

Trading cryptocurrencies carries significant risk.

