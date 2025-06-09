# 📊 PyLiveMarkets

**PyLiveMarkets** is a simple, terminal-based Python tool to check **real-time stock prices** from both the **Indian (NSE)** and **American (NASDAQ/NYSE)** markets. It uses the `yfinance` API for fetching stock data and `colorama` to enhance the output with colored terminal messages.

---

## 📁 Project Structure

```

PyLiveMarkets/
├── nse\_stock\_tracker.py        # Track Indian NSE stock prices
├── us\_stock\_tracker.py         # Track US stock prices (NASDAQ/NYSE)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

````

---

## 📦 Requirements

Ensure you have Python 3 installed, then install the required packages:

```bash
pip install -r requirements.txt
````

### requirements.txt

```
yfinance
colorama
```

---

## 🚀 How to Use

### 🇮🇳 Indian Market Tracker (NSE)

```bash
python nse_stock_tracker.py
```

**Sample Input:**

```
Enter the NSE stock symbol (e.g., TCS, INFY): tcs
```

**Sample Output:**

```
Current price of TCS (NSE): ₹3775.10
```

---

### 🇺🇸 US Market Tracker (NASDAQ/NYSE)

```bash
python us_stock_tracker.py
```

**Sample Input:**

```
Enter the stock symbol (e.g., AAPL, AMZN): amzn
```

**Sample Output:**

```
Current price of AMZN: $213.57
```

---

## 🧠 Behind the Scenes

* **`yfinance`** is used to fetch historical stock data and extract the most recent closing price.
* **`colorama`** adds colorful output to make the CLI more readable.

---

## ❗ Notes

* The NSE tracker adds `.NS` suffix to symbols (e.g., `TCS` → `TCS.NS`) as required by `yfinance`.
* Data is based on the most recent market close, not live-tick updates.
* Ensure you're connected to the internet for the API to work properly.

---

## 📜 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🙌 Contributions

Pull requests, issues, and feature suggestions are welcome. If you'd like to add BSE support, GUI version, or real-time charts — feel free to fork and build!

