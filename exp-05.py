import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("E:/Query processing/alphabet_stock_data.csv", parse_dates=['Date'], dayfirst=True)

# Filter the data for the specific date range
start_date = '2020-04-01'
end_date = '2020-04-30'
filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

# Create a bar plot for the trading volume
plt.figure(figsize=(10, 6))
plt.bar(filtered_data['Date'], filtered_data['Volume'], color='blue')
plt.title('Trading Volume of Alphabet Inc. Stock (April 2020)')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
