import pandas as pd
employees=pd.read_csv(r"E:/Query processing/Dep1.csv")
print("Distinct department_id:")
print(employees.DEPARTMENT_ID.unique())
