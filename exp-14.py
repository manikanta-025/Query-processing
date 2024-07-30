import pandas as pd
import numpy as np
data = {
'A': [1, 2, np.nan, 4, 5],
'B': [5, np.nan, 7, 8, np.nan],
'C': ['a', 'b', np.nan, 'd', 'e'],
'D': [10, 20, 30, np.nan, 50]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df['A'].fillna(df['A'].mean(), inplace=True)
df['B'].fillna(df['B'].mean(), inplace=True)
df['C'].fillna('Unknown', inplace=True)
df['D'].fillna(df['D'].mean(), inplace=True)
print("\nDataFrame after replacing missing values:")
print(df)
