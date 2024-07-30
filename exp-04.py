import pandas as pd
import matplotlib.pyplot as plt

# Data from the image
data = pd.read_csv("E:/Query processing/alphabet_stock_data.csv")

# Creating a DataFrame
stock_df = pd.DataFrame(data)

# Converting 'Date' column to datetime
stock_df['Date'] = pd.to_datetime(stock_df['Date'], format='%d-%m-%Y')

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(stock_df['Date'], stock_df['Close'], marker='o')
plt.title('Historical Stock Prices of Alphabet Inc. (April 2020 - May 2020)')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
