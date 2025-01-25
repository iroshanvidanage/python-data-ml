## SF Salary Exercise

import pandas as pd
import numpy as np
import os
import subprocess

current_path = subprocess.run('pwd', shell=True, capture_output=True, text=True)
print(current_path)

if not os.path.exists('/home/iroshanav/Documents/DataScience/python-data-ml/Pandas/Salaries.csv'):
    print('File not found')
    exit()

sal_df = pd.read_csv('/home/iroshanav/Documents/DataScience/python-data-ml/Pandas/Salaries.csv')
print(sal_df.head())

print(sal_df.info())

print(sal_df['BasePay'].head(10))

print(sal_df['BasePay'].sum())

print(sal_df['BasePay'].mean())
print(sal_df['OvertimePay'].max())
print(sal_df[sal_df['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])
print(sal_df[sal_df['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits'])
print(sal_df[sal_df['TotalPayBenefits']==sal_df['TotalPayBenefits'].max()]['EmployeeName'])
print(sal_df[sal_df['TotalPayBenefits']==sal_df['TotalPayBenefits'].min()]['EmployeeName'])
print(sal_df.groupby('Year').describe()['BasePay']['mean'])
print(sal_df['JobTitle'].nunique())
print(sal_df['JobTitle'].value_counts().head())
print(sum(sal_df[sal_df['Year']==2013]['JobTitle'].value_counts()==1))
chief_name_list = [x for x in list(sal_df['JobTitle']) if 'chief' in x.lower()]
print(len(chief_name_list))
sal_df['title_len']=sal_df['JobTitle'].apply(len)
print(sal_df[['title_len', 'TotalPayBenefits']].corr())