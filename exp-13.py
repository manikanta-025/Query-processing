import pandas as pd
import numpy as np
data = {'A': [1, 2, np.nan, 4, 5],
'B': [5, np.nan, 7, 8, 9],
'C': [1, 2, 3, np.nan, 5],
'D': [5, 6, 7, 8, np.nan]}
df = pd.DataFrame(data)
missing_values = df.isnull()
print(missing_values)
