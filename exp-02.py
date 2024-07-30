import pandas as pd

df = pd.read_csv("E:/Query processing/emp1.csv")

job_count = df.groupby('EMPLOYEE_ID')['JOB_ID'].count()

two_or_more_jobs = job_count[job_count >= 2]

print(two_or_more_jobs)
