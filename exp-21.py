import pandas as pd
df = pd.DataFrame({'Name': ['John', 'JANE', 'Mike', 'EMILY'],
'Age': [25, 30, 35, 28],
'City': ['New York', 'LONDON', 'Paris', 'TOKYO']})
def swap_case(s):
    return s.swapcase()
df['City_Swapped'] = df['City'].apply(swap_case)
print("Original DataFrame:")
print(df)
print("\nDataFrame with Swapped Cases in City Column:")
print(df[['Name', 'Age', 'City_Swapped']])
