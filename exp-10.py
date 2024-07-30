import pandas as pd
import numpy as np
np.random.seed(42)
df = pd.DataFrame(np.random.randint(-100, 100, size=(10, 4)), columns=['A', 'B', 'C',
'D'])
def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'
styled_df = df.style.applymap(color_negative_red)
print(df)
print("\nStyled DataFrame (negative in red, positive in black):")
styled_df
