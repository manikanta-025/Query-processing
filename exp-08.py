import pandas as pd
data = {
'OrderDate': ['1-6-18', '1-23-18', '2-9-18', '2-26-18', '3-15-18'],
'Region': ['East', 'Central', 'Central', 'Central', 'West'],
'Manager': ['Martha', 'Hermann', 'Hermann', 'Timothy', 'Timothy'],
'SalesMan': ['Alexander', 'Shelli', 'Luis', 'David', 'Stephen'],
'Item': ['Television', 'Home Theater', 'Television', 'Cell Phone', 'Television'],
'Units': [95, 50, 36, 27, 56],
'Unit_price': [1198.00, 500.00, 1198.00, 225.00, 1198.00],
'Sale_amt': [113810.00, 25000.00, 43128.00, 6075.00, 67088.00]
}
df = pd.DataFrame(data)
pivot_table = pd.pivot_table(df, values='Units', index='Item', aggfunc='sum')
print(pivot_table)
