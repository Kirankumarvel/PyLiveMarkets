import yfinance as yf
from colorama import Fore, Style, init

init(autoreset=True)

symbol = input(Fore.CYAN + "Enter the NSE stock symbol (e.g., TCS, INFY): ").upper()
nse_symbol = symbol + ".NS"  # NSE suffix

stock = yf.Ticker(nse_symbol)

try:
    price = stock.history(period="1d")["Close"].iloc[-1]
    print(
        Fore.GREEN + Style.BRIGHT +
        f"Current price of {Fore.YELLOW}{symbol}{Fore.GREEN}(NSE): {Fore.MAGENTA}₹{price:.2f}"
    )
except IndexError:
    print(Fore.RED + "Invalid stock symbol or no data available.")
