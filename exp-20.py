import pandas as pd
data = {'text': ['Python is awesome', 'Pandas is powerful', 'Data science is fun',
'Machine learning is exciting']}
df = pd.DataFrame(data)
substring = 'is'
df['substring_index'] = df['text'].str.find(substring)
print(df)
