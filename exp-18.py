import pandas as pd
data = {
'school_code': ['s001','s002','s001','s002','s001','s002'],
'class': ['V', 'V', 'VI', 'VI', 'VI', 'VII'],
'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
'date_of_birth':
['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
'age': [12, 12, 13, 13, 13, 12],
'height': [173, 192, 186, 167, 151, 159],
'weight': [35, 32, 33, 30, 31, 32],
'address': ['street1', 'street2', 'street3', 'street4', 'street5', 'street6']
}
df = pd.DataFrame(data)
grouped = df.groupby(['school_code', 'class'])
for name, group in grouped:
    print(f"School Code: {name[0]}, Class: {name[1]}")
    print(group)
    print()
