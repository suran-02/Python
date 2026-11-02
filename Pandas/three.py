import pandas as pd
import numpy as np
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
# df.loc[df.Name=='Jin','Salary'] = np.nan
# print(df.isnull().sum())
# df = df.fillna(0)
# print(df.isnull().sum())


### AGGREGATION & GROUP BY
# print(df['Role'].value_counts()) # frequency of values
# print(df[df['Role'] == 'Vocalist'].value_counts())

# print(df.groupby('Role')['Salary'].sum())

data1 = {
    'Name': ['Apple', 'Banana', 'Apple', 'Orange',
             'Banana', 'Apple', 'Orange'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit',
                 'Fruit', 'Fruit', 'Fruit'],
    'City': ['Hyderabad', 'Mumbai', 'Mumbai',
             'Hyderabad', 'Delhi', 'Delhi', 'Mumbai'],
    'Sales': [100, 200, 150, 300, 250, 400, 350],
    'Quantity': [2, 4, 3, 5, 5, 8, 7]
}

sales = pd.DataFrame(data1)

# print(sales.groupby(['City'])['Sales'].agg(
#     ['sum','mean','min','max','count']
# ))

# print(sales.groupby(['City']).agg(
#     {
#         'Sales':'mean',
#         'Quantity':'sum'
#     }
# ))


### CONCATENATE AND MERGE DATAFRAMES (JOINS)
df2 = pd.DataFrame({
    'ID':[1,2,3],
    'Name':['A','B','C']
})
df3 = pd.DataFrame({
    'ID':[1,2,3,4],
    'Score':[88,96,77,79]
})

print(pd.concat([df2,df3], axis=0)) ## vertical join/ row-level / top on top

print(pd.concat([df2,df3],axis=1)) ## horizontal join/ column-level / side by side

## MERGE = JOIN
print(pd.merge(df2,df3,how='inner',on='ID'))
print(pd.merge(df2,df3,how='outer',left_on='ID',right_on='ID'))

