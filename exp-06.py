import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('alphabet_stock_data.csv', parse_dates=['Date'], dayfirst=True)

# Filter the data for the specific date range
start_date = '2020-04-01'
end_date = '2020-04-30'
filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

# Create a scatter plot for trading volume vs stock prices
plt.figure(figsize=(10, 6))
plt.scatter(filtered_data['Volume'], filtered_data['Close'], color='green')
plt.title('Trading Volume vs Stock Prices of Alphabet Inc. (April 2020)')
plt.xlabel('Trading Volume')
plt.ylabel('Stock Prices (Close)')
plt.grid()
plt.tight_layout()
plt.show()
