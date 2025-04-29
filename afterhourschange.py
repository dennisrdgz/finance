import yfinance as yf
import pandas as pd

stonks = [
    'AAPL', 'ACI', 'ADSK', 'AMC', 'AMD', 'AMLP', 'AMZN', 'AMZY', 'APD', 'APLE', 'APLY', 'ARM',
    'AVGO', 'BK', 'BRK-A', 'BRK-B', 'BTI', 'C', 'CAVA', 'CBOE', 'CLM', 'CME', 'CMG', 'COF',
    'COIN', 'COLM', 'COST', 'CP', 'CQQQ', 'CRM', 'CRWD', 'CVX', 'DAX', 'DIA', 'EDIT', 'ET',
    'EWG', 'EWJ', 'EWP', 'EWQ', 'EWU', 'EWW', 'FNGS', 'FNGA', 'GBTC', 'GEO', 'GLD', 'GOOGL',
    'GS', 'HMC', 'HPE', 'IBIT', 'IEP', 'INTC', 'IONQ', 'KLIP', 'KR', 'KTOS', 'KWEB', 'LHX',
    'LIN', 'LLY', 'MA', 'MCD', 'MCHI', 'MMM', 'MS', 'MSFT', 'MSTR', 'MU', 'NFLX', 'NOW',
    'NVDA', 'OXY', 'PAYX', 'PGR', 'PLD', 'PLTR', 'PM', 'QQQ', 'RTX', 'SHLD', 'SMH', 'SMHX',
    'SOFI', 'SPDW', 'SPY', 'SSB', 'T', 'THC', 'TLT', 'TM', 'TMF', 'TMV', 'TQQQ', 'TSLA',
    'TSLY', 'TSM', 'UAL', 'UDOW', 'UNH', 'UPRO', 'V', 'VICI', 'VLO', 'VRT', 'WES', 'WM',
    'WMT', 'WTI', 'WWR', 'X', 'XLE', 'XLF', 'XLP', 'XOM','SAN'
]

df = pd.DataFrame(columns=("Stonk", "%Change"))
failed_tickers = []

for x in stonks:
    try:
        data = yf.download(x, period='1d', interval='1m', prepost=True, progress=False)
        close = yf.download(x, period='1d', interval='1m', prepost=False, progress=False)

        if data.empty or close.empty:
            raise ValueError("Empty data frame returned")

        perc = (data.iloc[-1, 3] - close.iloc[-1, 3]) * 100 / close.iloc[-1, 3]
        perc = round(perc, 3)

        df.loc[len(df)] = [x, perc]

    except Exception as e:
        failed_tickers.append(x)
        print(f"Error with {x}: {e}")

# Display results
print("\nSorted DataFrame:")
print(df.sort_values("%Change", ascending=False))

if failed_tickers:
    print("\nThe following tickers failed and were skipped:")
    print(failed_tickers)

# Sort DataFrame
sorted_df = df.sort_values("%Change", ascending=False)

# Display results
print("\nSorted DataFrame:")
print(sorted_df)

# Save to Excel
save_path = r"C:\Users\denni\iCloudDrive\APEX FINANCIAL SOLUTIONS INC\Coding\stonks_output.xlsx"
sorted_df.to_excel(save_path, index=False)

print(f"\nSaved sorted DataFrame to:\n{save_path}")

if failed_tickers:
    print("\nThe following tickers failed and were skipped:")
    print(failed_tickers)   