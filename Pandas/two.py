### ROWS & COLUMNS OPERATIONS
import pandas as pd
data = {
    "Name": ["RM","Jin","Suga","JHope"],
    "Age":[29,34,30,29],
    "Salary":[100000,80000,90000,95000]
}

df = pd.DataFrame(data)

## Add new column
df['Role'] = ['Leader','Vocalist','Rapper','Dancer']
# print(df)
# print()
df['Bonus'] = df['Salary'] * 0.3
# print(df)

## Add new row
df.loc[len(df)] = ["Taehyung",28,95000,"Vocalist",30000]
# print(df)
# print(len(df))

## Update value - using index name
df.loc[0,"Salary"] = 150000
# print(df)

## Update value - using column name
df.loc[df.Name == 'Taehyung','Bonus'] = 50000
# print(df)


### DELETE ROWS & COLUMNS

## Getting a full row
# print(df[df.Name == 'Taehyung'])
# print(df[df['Name']=='Taehyung'])

## Deleting rows
# df = df.drop(df[df.Name == 'Taehyung'].index)
## Deleting columns
# df.drop('Bonus',axis=1, inplace=True)

## Deleting multiple columns
# df.drop(['Bonus','Role'],axis=1,inplace=True)
# print(df)


### SORTING
df = df.sort_values('Bonus', ascending=False)
print(df)