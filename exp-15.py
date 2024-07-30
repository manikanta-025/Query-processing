import pandas as pd
import numpy as np
data = {
'A': [1, 2, np.nan, 4, 5],
'B': [np.nan, 2, 3, np.nan, 5],
'C': [1, 2, 3, 4, np.nan],
'D': [np.nan, np.nan, 3, 4, 5]
}
df = pd.DataFrame(data)
mask = df.isna().sum(axis=1) >= 2
result = df[mask]
print("Original DataFrame:")
print(df)
print("\nDataFrame with rows having at least 2 NaN values:")
print(result)
