import pandas as pd
import numpy as np
np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])
df.iloc[1, 2] = np.nan
df.iloc[3, 0] = np.nan
df.iloc[7, 1] = np.nan
def highlight_nan(val):
    return 'background-color: yellow' if pd.isna(val) else ''
styled_df = df.style.applymap(highlight_nan)
print(styled_df)
