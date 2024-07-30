import pandas as pd
data = {
'school_code': ['s001','s002','s001','s002','s001','s001','s002','s002'],
'class': ['V', 'V', 'VI', 'VI', 'V', 'VI', 'V', 'V'],
'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes', 'Parth Patel', 'Ricky Ahuja'],
'date_of_birth':['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997','19/08/2004','12/06/2003'],
'age': [12, 12, 13, 13, 13, 12, 12, 12],
'height': [173, 192, 186, 167, 151, 159, 199, 201],
'weight': [35, 32, 33, 30, 31, 32, 30, 34]
}
df = pd.DataFrame(data)
grouped = df.groupby('school_code')
print("Type of GroupBy object:")
print(type(grouped))
print("\nGroups:")
for name, group in grouped:
    print(f"\nSchool Code: {name}")
    print(group)
