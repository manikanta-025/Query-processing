import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("alphabet_stock_data.csv")
data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')
data.set_index('Date', inplace=True)

plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Open'], label='Open')
plt.plot(data.index, data['High'], label='High')
plt.plot(data.index, data['Low'], label='Low')
plt.plot(data.index, data['Close'], label='Close')
plt.title('Alphabet Inc. Stock Prices (Oct 3-7, 2016)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
