import yfinance as yf
import csv
from datetime import datetime
from pathlib import Path

from colorama import Fore, Style, init
init(autoreset=True)

input_file = "stock_list.csv"
output_file = "stock_prices_log.csv"

today = datetime.today().strftime('%Y-%m-%d')
log_exists = Path(output_file).exists()

with open(input_file, 'r') as file:
    reader = csv.DictReader(file)
    stocks = list(reader)

with open(output_file, 'a', newline='') as file:
    fieldnames = ['date', 'symbol', 'region', 'price']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    if not log_exists:
        writer.writeheader()

    for stock in stocks:
        symbol = stock['symbol'].strip().upper()
        region = stock['region'].strip().upper()

        if region == 'IN':
            yf_symbol = symbol + '.NS'
        elif region == 'US':
            yf_symbol = symbol
        else:
            print(Fore.RED + f"Invalid region for {symbol}: {region}")
            continue

        try:
            ticker = yf.Ticker(yf_symbol)
            price = ticker.history(period="1d")["Close"].iloc[-1]
            writer.writerow({'date': today, 'symbol': symbol, 'region': region, 'price': round(price, 2)})

            print(
                Fore.GREEN + f"{symbol} ({region}) - " +
                Fore.YELLOW + f"{'₹' if region == 'IN' else '$'}{price:.2f}"
            )
        except Exception as e:
            print(Fore.RED + f"Failed to fetch data for {symbol}: {e}")
