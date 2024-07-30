import pandas as pd
import numpy as np
np.random.seed(42)
df = pd.DataFrame(np.random.randint(0, 100, size=(10, 4)), columns=['A', 'B', 'C',
'D'])
print(df)
def style_df(val):
    return 'background-color: black; color: yellow'
styled_df = df.style.map(style_df)
print(styled_df)
