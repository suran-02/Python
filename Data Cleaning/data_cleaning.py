import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('messy_customer_sales_data.csv')
# print(df)

#checking the problems

# df.info()
# print(df.describe().round())
# print(df.isnull().sum())
# print(df.isnull().sum()/len(df) * 100)
# print(df[df.duplicated()])
# print(df['Customer_ID'].value_counts().head())
for col in df.columns:
    if df[col].nunique()<20:
        print(df[col].value_counts())
        print('-'*20)