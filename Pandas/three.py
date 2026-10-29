import pandas as pd
data = {
    "Name": ["RM","Jin","Suga","JHope"],
    "Age":[29,34,30,29],
    "Salary":[100000,80000,90000,95000]
}

df = pd.DataFrame(data)
df['Role'] = ['Leader','Vocalist','Rapper','Dancer']
df.loc[len(df)] = ["Taehyung",28,95000,"Vocalist"]


### HANDLING DATE AND TIME
df['DOJ'] = ['2012-01-20','2012-03-15','2012-05-01','2012-02-28','2012-09-04']
print(df['DOJ'].dtype) # string
df['DOJ'] = pd.to_datetime(df['DOJ'])
print(df['DOJ'].dtype)

## Example of wrong date format
# df1 = df
# df1['DOJ2'] = ['01-02-2012','21-09-2012','12-07-2012','09-11-2012','17-10-2012']
# print(df1['DOJ2'].dtype)
## then fixing it
# df1['DOJ2'] = pd.to_datetime(df1['DOJ2'],format='%d-%m-%Y')
# print(df1['DOJ2'].dtype)

## Extract year, month, week, day

# print(df['DOJ'].dt.year)
# print(df['DOJ'].dt.month)
# print(df['DOJ'].dt.day)
# print(df['DOJ'].dt.day_name())
df['Day'] = df['DOJ'].dt.day_name()
# print(df)


## Adding values to dates

# df['End_of_Contract'] = df['DOJ'] + pd.Timedelta(days=1000)
# df.drop('End_of_Contract',axis=1)
# print(df)

### HANDLING MISSING VALUES

