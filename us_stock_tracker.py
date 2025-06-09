import yfinance as yf
from colorama import Fore, Style, init

init(autoreset=True)

symbol = input(Fore.CYAN + "Enter the stock symbol (e.g., AAPL, AMZN): ").upper()
stock = yf.Ticker(symbol)

try:
    price = stock.history(period="1d")["Close"].iloc[-1]
    print(Fore.GREEN + f"Current price of {symbol}: " + Fore.YELLOW + f"${price:.2f}")
except IndexError:
    print(Fore.RED + "Invalid stock symbol or no data available.")
