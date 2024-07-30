import pandas as pd
data = {
'Country': ['USA', 'UK', 'France', 'Germany', 'Italy'],
'Beer': [50, 40, 35, 60, 25],
'Wine': [20, 25, 45, 30, 35],
'Spirit': [30, 35, 20, 10, 40]
}
df = pd.DataFrame(data)
print("Dimensions of the dataset:")
print(df.shape)
print("\nColumn names:")
print(df.columns.tolist())
