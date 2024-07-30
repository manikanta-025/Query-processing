import pandas as pd
data = {
'Item': ['Television', 'Home Theater', 'Cell Phone', 'Television', 'Home Theater']
* 2,
'Sale_amt': [113810, 25000, 6075, 67088, 30000, 89850, 107820, 38336, 30000,
107820]
}
df = pd.DataFrame(data)
pivot_table = pd.pivot_table(df, values='Sale_amt', index='Item', aggfunc=['max',
'min'])
print(pivot_table)
