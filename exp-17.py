import pandas as pd
data = {
'school_code': ['s001','s002','s001','s002','s001','s001','s002','s002'],
'class': ['V', 'V', 'VI', 'VI', 'VI', 'VII', 'VII', 'VIII'],
'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes', 'Alberto Franco', 'Eesha Hinton'],
'age': [12, 12, 13, 13, 13, 14, 14, 15]
}
df = pd.DataFrame(data)
result = df.groupby('school_code')['age'].agg(['mean', 'min', 'max'])
print(result)
