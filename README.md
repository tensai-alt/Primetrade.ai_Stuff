# 🚀 Binance Futures Testnet Trading Bot

A modular Python trading bot that places **MARKET**, **LIMIT**, and **STOP-LIMIT** orders on Binance Futures Testnet (USDT-M), with proper validation, logging, retry handling, and a clean CLI interface.

---

## 📌 Features

* ✅ MARKET orders
* ✅ LIMIT orders
* ✅ STOP-LIMIT orders *(extra 🥲)*
* ✅ BUY / SELL support
* ✅ CLI interface using Typer + Rich
* ✅ Input validation and error handling
* ✅ Structured logging (requests, responses, errors)
* ✅ Retry mechanism with exponential backoff
* ✅ Clean modular architecture

---

## 🏗️ Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance API wrapper
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── retry.py           # Retry mechanism
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point (Typer)
├── requirements.txt
├── README.md
└── logs/
```

---

## ⚙️ Setup

### 1. Clone repository

```
git clone https://github.com/tensai-alt/Primetrade.ai_Stuff.git
cd trading_bot
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Create `.env` file

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

👉 Uses Binance Futures Testnet:
https://testnet.binancefuture.com

---

## ▶️ Usage

### 🔹 MARKET Order

```
python cli.py trade \
  --symbol BTCUSDT \
  --side BUY \
  --order-type MARKET \
  --quantity 0.001
```

---

### 🔹 LIMIT Order

```
python cli.py trade \
  --symbol BTCUSDT \
  --side SELL \
  --order-type LIMIT \
  --quantity 0.001 \
  --price 70000
```

---

### 🔹 STOP-LIMIT Order

```
python cli.py trade \
  --symbol BTCUSDT \
  --side BUY \
  --order-type STOP_LIMIT \
  --quantity 0.001 \
  --price 68000 \
  --stop-price 68500
```

---

## 📊 Output Example

```
Order Summary
Symbol      : BTCUSDT
Side        : BUY
Type        : MARKET
Quantity    : 0.001

Order Successful
Order ID     : 12345678
Status       : FILLED
Executed Qty : 0.001
Avg Price    : 69234.50
```

---

## 📝 Logging

Logs are stored in:

```
logs/trading_bot.log
```

### Example Logs

```
[REQUEST] {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.001}
[RESPONSE] {...}
[WARNING] Retry 1/3 after error: Network issue
[ERROR] ...
```

---

## 🧪 Test Results (Assignment Requirement)

### ✅ MARKET Order Test

* Symbol: BTCUSDT
* Side: BUY
* Type: MARKET
* Status: SUCCESS

```
Order ID: XXXXX
Status: FILLED
Executed Qty: 0.001
```

---

### ✅ LIMIT Order Test
* Symbol: BTCUSDT
* Side: SELL
* Type: LIMIT
* Price: 70000
* Status: SUCCESS

```
Order ID: XXXXX
Status: NEW / FILLED
```

---

### ✅ STOP-LIMIT Order Test (Extra 🥲)
* Symbol: BTCUSDT
* Side: BUY
* Stop Price: 68500
* Limit Price: 68000
* Status: SUCCESS

---

## ⚠️ Assumptions
* Uses Binance Futures Testnet (USDT-M)
* No leverage/margin configuration included
* No position tracking implemented
* Basic validation only (not exchange-level precision validation)

---

## 🧠 Design Decisions

* **Client Layer (`client.py`)**
  Encapsulates Binance API interaction

* **Service Layer (`orders.py`)**
  Handles business logic and order construction

* **Validation Layer (`validators.py`)**
  Ensures safe and correct inputs

* **Retry Layer (`retry.py`)**
  Handles transient failures (network/API)

* **CLI Layer (`cli.py`)**
  User interface using Typer

---

## 🚀 Future Improvements
* WebSocket price streaming
* Strategy engine (EMA / RSI)
* Position & PnL tracking
* Order book analysis
* Risk management module

---

## 📬 Submission Notes
* All required features implemented
* Bonus features included (Stop-Limit, retry, enhanced CLI)
* Logs generated from real testnet executions
* Clean, modular, and extensible design

---

## 👤 Author
Rohit Kumar Swain
