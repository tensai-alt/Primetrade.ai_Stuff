# 🚀 Binance Futures Testnet Trading Bot

A modular Python trading bot that places **MARKET**, **LIMIT**, and **STOP-LIMIT** orders on Binance Futures Demo API (USDT-M), with proper validation, logging, retry handling, and a clean CLI interface.

---

## 📌 Features

- ✅ MARKET orders  
- ✅ LIMIT orders  
- ✅ STOP-LIMIT orders *(extra 🥲)*  
- ✅ BUY / SELL support  
- ✅ CLI interface using Typer + Rich  
- ✅ Input validation and error handling  
- ✅ Structured logging (requests, responses, errors)  
- ✅ Retry mechanism with exponential backoff  
- ✅ Clean modular architecture  

---

## 🏗️ Project Structure

```text
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── retry.py
│   ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
└── logs/
```

---

## ⚙️ Setup

### 1. Clone repository

```bash
git clone https://github.com/tensai-alt/Primetrade.ai_Stuff.git
cd trading_bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` file

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

👉 Uses Binance Futures Demo API:  
https://demo-fapi.binance.com

---

## ▶️ Usage

### 🔹 MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

---

### 🔹 LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 76000
```

---

### 🔹 STOP-LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type STOP_LIMIT --quantity 0.001 --price 68000 --stop-price 68500
```

---

## 📊 Output Example

```text
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

```text
logs/trading_bot.log
```

### Example Logs

```text
[REQUEST] {...}
[RESPONSE] {...}
[ERROR] ...
```

---

## 🧪 Test Results

---

### ✅ MARKET Order Test

- Symbol: BTCUSDT  
- Side: BUY  
- Type: MARKET  

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

```text
Order ID: XXXXX
Status: FILLED
Executed Qty: 0.001
```

<img width="1200" height="357" alt="image" src="https://github.com/user-attachments/assets/6f7faa21-b6d8-4076-86e7-2c4d92dc62c1" />


---

### ✅ LIMIT Order Test

- Symbol: BTCUSDT  
- Side: SELL  
- Type: LIMIT  

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 76000
```

```text
Order ID: XXXXX
Status: NEW / FILLED
```

<img width="1319" height="360" alt="image" src="https://github.com/user-attachments/assets/558614ec-712e-44e2-9d81-609512b1ff22" />


---

### ✅ STOP-LIMIT Order Test

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type STOP_LIMIT --quantity 0.001 --price 68000 --stop-price 68500
```

```text
Order ID: XXXXX
Status: NEW / FILLED
```

### This extra feature is not working, I was just casually trying to develop this STOP_LOSS feature

---

## ⚠️ Assumptions

- Uses Binance Futures Demo API  
- No leverage/margin config  
- No position tracking  
- Basic validation only  

---

## 🧠 Design Decisions

- client.py → API handling  
- orders.py → order logic  
- validators.py → validation  
- retry.py → retry mechanism  
- cli.py → user interface  

---

## 🚀 Future Improvements

- WebSocket streaming  
- Strategy engine  
- PnL tracking  
- Risk management  

---

## 📬 Submission Notes

- All required features implemented  
- Bonus features included  
- Logs generated from demo API  
- Clean modular design  

---

## 👤 Author

Rohit Kumar Swain
